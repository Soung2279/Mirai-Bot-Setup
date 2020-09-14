from io import BytesIO
from os import path
import requests
from PIL import Image,ImageFont,ImageDraw
from hoshino import Service, priv
from hoshino.util import FreqLimiter,fig2b64
import matplotlib.pyplot as plt
from .data_source import get_data, get_person, get_time
from matplotlib import font_manager as fm
import base64
import pandas as pd
import numpy as np
import datetime
import math
from nonebot import MessageSegment as ms

_time_limit = 1*60
_lmt = FreqLimiter(_time_limit)

font_path = path.join(path.dirname(__file__), 'msyh.ttf')

b_constellations = ["摩羯","水瓶","双鱼","白羊","金牛","双子","巨蟹","狮子","处女","天秤","天蝎","射手"] #国服的（预测）

background1 = '公会离职报告模板.jpg'
background2 = '公会本期报告模板.jpg'

REPORT_RESIGN = 0
REPORT_NORMAL = 1
REPORT_UNDECLARED = -1

sv_help = '''
[离职报告/会战报告] 生成一张离职报告/会战报告
[看看报告@qq] 看看群员的会战报告（限管理员）
[出刀时间统计] 生成一张出刀时间分布表
'''.strip()

sv = Service('report-hoshino', help_=sv_help, bundle='pcr会战')

@sv.on_fullmatch(('!离职报告','！离职报告'))
async def send_resign_report(bot, event):
    uid = event['user_id']
    nickname = event['sender']['card'] or event['sender']['card']
    gid = event['group_id']
    report = gen_report(gid, uid, nickname, type=REPORT_RESIGN)
    await bot.send(event, report)

@sv.on_fullmatch(('!会战报告','！会战报告'))
async def send_normal_report(bot, event):
    uid = event['user_id']
    nickname = event['sender']['card'] or event['sender']['card']
    gid = event['group_id']
    report = gen_report(gid, uid, nickname, type=REPORT_NORMAL)
    await bot.send(event, report)

#罪恶的功能，不启用了
#@sv.on_prefix(('看看报告','查看报告'))
async def send_others_report(bot, event):
    if not priv.check_priv(event, priv.ADMIN):
        await bot.send(event, f'查看他人的报告需要群管理权限哦！')
        return

    gid = event['group_id']
    message = event['message']
    nickname,uid = None,None
    for msg in message:
        if msg.type == 'at' and msg.data['qq'] != 'all':
            uid = int(msg.data['qq'])
            info = await bot.get_group_member_info(group_id=gid,user_id=uid)
            nickname = info['card'] or info['nickname']

    if nickname:
        msg = gen_report(gid,uid,nickname,type=REPORT_NORMAL,kpi=True)
    else:
        msg = '参数错误！'
    await bot.send(event, msg)

#这个函数本来可以直接写的，但为了保证代码风格统一就再封装一层
@sv.on_fullmatch(('!出刀时间统计','！出刀时间统计'))
async def send_chal_stat(bot, event):
    await send_time_dist(bot, event)

def gen_report(gid, uid, nickname, type=REPORT_UNDECLARED, kpi=False):

    if type not in (REPORT_RESIGN,REPORT_NORMAL):
        return "类型错误！"
    if not kpi:
        if not _lmt.check(uid):
            return f'每{math.ceil(_time_limit/60)}分钟仅能生成一次报告'
        _lmt.start_cd(uid)

    year,month = get_ym()
    constellation = b_constellations[month-1]

    try:
        clanname, challenges = get_person(gid,uid,year,month)
    except Exception as e:
        return f"出现错误: {str(e)}\n请联系开发组调教。"
    if challenges.shape[0] == 0:
        return "您没有参加本次公会战。请再接再厉！"

    total_chl = 0
    miss_chl = 0
    damage_to_boss: list = [0 for i in range(5)]
    times_to_boss: list = [0 for i in range(5)]
    truetimes_to_boss: list = [0 for i in range(5)]
    total_damage = 0

    for idx,chl in challenges.iterrows():
        total_damage += chl['dmg']
        times_to_boss[chl['boss']-1] += 1
        if chl['flag'] == 0:
            damage_to_boss[chl['boss']-1] += chl['dmg']
            truetimes_to_boss[chl['boss']-1] += 1
        if chl['flag'] != 1:
            total_chl += 1
        if chl['dmg'] == 0:
        	miss_chl += 1

    avg_day_damage = int(total_damage/6)
    df=pd.DataFrame({'a':damage_to_boss,'b':truetimes_to_boss})
    result=(df.a/df.b).replace(np.inf,0).fillna(0)
    avg_boss_damage = list(result)
    if total_chl >= 18:
        disable_chl = 0
        attendance_rate = 100
    else:
        disable_chl = 18 - total_chl
        attendance_rate = round(total_chl/18*100,2)

    #日期转字符串
    year=str(year)
    month=str(month)
    
    #设置中文字体
    plt.rcParams['font.family'] = ['Microsoft YaHei']
    x = [f'{x}王' for x in range(1,6)]
    y = times_to_boss
    plt.figure(figsize=(4.3,2.8))
    ax = plt.axes()

    #设置标签大小
    plt.tick_params(labelsize=15)

    #设置y轴不显示刻度
    plt.yticks([])

    #绘制刀数柱状图
    recs = ax.bar(x,y,width=0.618,color=['#fd7fb0','#ffeb6b','#7cc6f9','#9999ff','orange'],alpha=0.4)

    #删除边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    #设置数量显示
    for i in range(0,5):
        rec = recs[i]
        h = rec.get_height()
        plt.text(rec.get_x()+0.1, h, f'{int(times_to_boss[i])}刀',fontdict={"size":12})
    buf = BytesIO()
    plt.savefig(buf, format='png', transparent=True, dpi=120)
    bar_img1 = Image.open(buf)
    #清空图
    plt.clf()

    x = [f'{x}王' for x in range(1,6)]
    y = avg_boss_damage
    plt.figure(figsize=(4.3,2.8))
    ax = plt.axes()

    #设置标签大小
    plt.tick_params(labelsize=15)

    #设置y轴不显示刻度
    plt.yticks([])

    #绘制均伤柱状图
    recs = ax.bar(x,y,width=0.618,color=['#fd7fb0','#ffeb6b','#7cc6f9','#9999ff','orange'],alpha=0.4)

    #删除边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    #设置数量显示
    for i in range(0,5):
        rec = recs[i]
        h = rec.get_height()
        plt.text(rec.get_x(), h, f'{int(avg_boss_damage[i]/10000)}万',fontdict={"size":12})

    buf = BytesIO()
    plt.savefig(buf, format='png', transparent=True, dpi=120)
    bar_img2 = Image.open(buf)

    #将饼图和柱状图粘贴到模板图,mask参数控制alpha通道，括号的数值对是偏移的坐标
    current_folder = path.dirname(__file__)
    img = Image.open(path.join(current_folder,background1 if type==REPORT_RESIGN else background2))
    img.paste(bar_img1, (580,950), mask=bar_img1.split()[3])
    img.paste(bar_img2, (130,950), mask=bar_img2.split()[3])

    #添加文字到img
    row1 = f'''
    {total_chl}

    {disable_chl}

    {total_damage}
    '''
    row2 = f'''
    {attendance_rate}%

    {miss_chl}

    {avg_day_damage}
    '''
    
    add_text(img, row1, position=(400,620), textsize=35, textfill='black')
    add_text(img, row2, position=(850,620), textsize=35, textfill='black')
    add_text(img, year, position=(355,438), textsize=40, textfill='black')
    add_text(img, month, position=(565,438), textsize=40, textfill='black')
    add_text(img, constellation, position=(710,438), textsize=40, textfill='black')
    if len(clanname) <= 7:
        add_text(img, clanname, position=(300+(7-len(clanname))/2*40, 515), textsize=40, textfill='black')
    else:
        add_text(img, clanname, position=(300+(10-len(clanname))/2*30, 520), textsize=30, textfill='black')
    add_text(img, nickname, position=(280,365), textsize=35, textfill='white')
    #输出
    buf = BytesIO()
    img.save(buf,format='JPEG')
    base64_str = f'base64://{base64.b64encode(buf.getvalue()).decode()}'
    img = f'[CQ:image,file={base64_str}]'
    plt.close('all')
    return img

async def send_time_dist(bot, event):
    gid = event['group_id']
    year,month = get_ym()

    try:
        name,times = get_time(gid,year,month)
    except Exception as e:
        await bot.send(event, f"出现错误: {str(e)}\n请联系开发组调教。")
        return

    plt.rcParams['axes.unicode_minus']=False
    prop = fm.FontProperties(fname=font_path)
    prop.set_size('large')
    fig,ax = plt.subplots(figsize=(12,6),facecolor='white')
    ax.set_xlabel('时间',fontproperties=prop)
    ax.set_ylabel('刀数',fontproperties=prop)
    ax.set_title(f'{name}{year}年{month}月会战出刀时间统计',fontproperties=prop)
    ax.set_xlim((0-0.5,24))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    colors=(['#808080']*6)+(['#9bc5af']*6)+(['#c54731']*6)+(['#3a4a59']*6)
    plt.xticks(range(24),fontproperties=prop)
    plt.bar(range(24),times,color=colors)

    pic = fig2b64(plt)
    plt.close()
    await bot.send(event, ms.image(pic))

def get_ym():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if day < 20:
        month -= 1
    if month == 0:
        year -= 1
        month = 12
    return year,month

def add_text(img: Image,text:str,textsize:int,font=font_path,textfill='white',position:tuple=(0,0)):
    img_font = ImageFont.truetype(font=font,size=textsize)
    draw = ImageDraw.Draw(img)
    draw.text(xy=position,text=text,font=img_font,fill=textfill)
    return img