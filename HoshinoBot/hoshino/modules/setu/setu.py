import os
import random

from nonebot.exceptions import CQHttpError

from hoshino import R, Service, priv
from hoshino.util import FreqLimiter, DailyNumberLimiter
from hoshino.typing import CQEvent

_max = 20
_nlmt = DailyNumberLimiter(_max)
#每人日调用上限
_cd = 3
_flmt = FreqLimiter(_cd)
#调用冷却
EXCEED_NOTICE = f'您今天已经冲过{_max}次了，请明日再来或请求群管重置次数哦！'

sv = Service('setu', manage_priv=priv.ADMIN, enable_on_default=True, visible=True)
setu_folder = R.img('setu/').path
#本地涩图目录
def setu_gener():
    while True:
        filelist = os.listdir(setu_folder)
        random.shuffle(filelist)
        for filename in filelist:
            if os.path.isfile(os.path.join(setu_folder, filename)):
                yield R.img('setu/', filename)

setu_gener = setu_gener()

def get_setu():
    return setu_gener.__next__()

@sv.on_fullmatch(('不够色', '不够涩', '不够瑟', '来点色图', '来点涩图', '来点瑟图', '再来点', '看过了', '涩图', '色图', '瑟图', '铜', '来一份瑟图', '来一份色图', '来一份涩图', '我要看涩图', '我要看色图', '我要看瑟图', '铯'))
async def setu(bot, ev):
    """随机叫一份涩图，对每个用户有冷却时间"""
    uid = ev['user_id']
    if not _nlmt.check(uid):
        await bot.send(ev, EXCEED_NOTICE, at_sender=True)
        return
    if not _flmt.check(uid):
        await bot.send(ev, f"您冲得太快了，有{_cd}秒冷却哦", at_sender=True)
        return
    _flmt.start_cd(uid)
    _nlmt.increase(uid)

    pic = get_setu()
    try:
        await bot.send(ev, pic.cqcode)
    except CQHttpError:
        sv.logger.error(f"发送图片{pic.path}失败")
        try:
            await bot.send(ev, '涩图太涩，发不出去勒...')
        except:
            pass

@sv.on_prefix(('换肾', '补肾', '换弹夹', '换蛋夹'))
async def resetsetu(bot, ev: CQEvent):
    if not priv.check_priv(ev, priv.ADMIN):
        await bot.send(ev, '您的权限不足！请联系群管哦~')
        return
    count = 0
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            uid = int(m.data['qq'])
            _nlmt.reset(uid)
            count += 1
    if count:
        await bot.send(ev, f"已为{count}位用户重置次数！注意身体哦～")