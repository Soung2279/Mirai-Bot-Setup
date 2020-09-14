import asyncio
import re
import threading

import nonebot
from nonebot import NLPSession, on_natural_language, NLPResult, on_command, IntentCommand
from nonebot.command import Command, CommandSession
from .wife_config import *
from hoshino import Service

wife_lists = user_list()

sv = Service('laopo', enable_on_default=False)

@nonebot.scheduler.scheduled_job(
    'cron',
    day='*',
    hour='7',
    minute='30'
)
async def hunsband_goodMorning():
    bot = nonebot.get_bot()
    for i in wife_lists.all_user:
        try:
            await bot.send_private_msg(user_id=i.id, message='老公早安!')
            await bot.send_private_msg(user_id=i.id, message=await get_love_scence())
        except:
            pass


@nonebot.scheduler.scheduled_job(
    'cron',
    day='*'
)
async def ToDayisTalk():
    bot = nonebot.get_bot()
    try:
        for i in wife_lists.user_wife_list:
            if i.isTalk is True:
                i.isTalk = False
            else:
                i.liking -= 2
                await bot.send_private_msg(user_id=i.husband, message='你今天一天都没理我！(扣除2点好感度)')
    except:
        await bot.send_private_msg(user_id=1351495774, message="扣除好感度出错！")
        return
    await  write(wife_lists)


async def read():
    try:
        with open('index.json', 'r+', encoding='utf-8') as f:
            line = f.readline()
            while line:
                line = str(line).replace('[', '').replace(',\n', '').replace(']', '')
                t = json.loads(line)
                user_id = t['husband']
                temp_wife = wife(user_id)
                temp_wife.height = t['height']
                temp_wife.weight = t['weight']
                temp_wife.name = t['name']
                temp_wife.ouBai = t['ouBai']
                temp_wife.liking = t['liking']
                temp_wife.Character = t['character']
                temp_wife.age = t['age']
                temp_wife.isMerry = t['isMerry']
                temp_wife.work = t['work']
                temp_wife.race = t['race']
                temp_wife.bud = t['bud']
                temp_wife.husband = t['husband']
                await wife_lists.add_user(temp_wife)
                wife_lists.all_user.append(user(user_id))
                line = f.readline()
            f.close()
    except:
        try:
            with open('index.json', 'r+', encoding='utf-8') as f:
                line = f.readline()
                while line:
                    line = str(line).replace('[', '').replace(',\n', '').replace(']', '')
                    t = json.loads(line)
                    user_id = t['husband']
                    temp_wife = wife(user_id)
                    temp_wife.height = t['height']
                    temp_wife.weight = t['widget']
                    temp_wife.name = t['name']
                    temp_wife.ouBai = t['ouPai']
                    temp_wife.liking = t['liking']
                    temp_wife.Character = t['sex']
                    temp_wife.age = t['age']
                    temp_wife.isMerry = t['isMerry']
                    temp_wife.work = t['work']
                    temp_wife.race = t['race']
                    temp_wife.bud = t['meng']
                    temp_wife.husband = t['husband']
                    await  wife_lists.add_user(temp_wife)
                    wife_lists.all_user.append(user(user_id))
                    line = f.readline()
            f.close()
        except:
            with open('index.json', 'a+', encoding='utf-8') as f:
                f.close()
    return


@sv.on_command('fuckingIndex', aliases='我的渣男值', only_to_me=False)
async def wife_self_index(session: NLPSession):
    send_user = session.event['user_id']
    for i in wife_lists.all_user:
        if i.id == send_user:
            await session.send(message=str(i.fuckingBoy), at_sender=True)
            break
    else:
        await session.send(message="没有找到你的信息", at_sender=True)


@sv.on_command('wife', aliases=('老婆'), only_to_me=False)
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
async def _(session: NLPSession):
    if not wife_lists.alredyInit:
        await read()
        wife_lists.alredyInit = True
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                if i.isTalk is False:
                    i.isTalk = True
                await session.send(message=f'我是{i.name},老公你找我啊', at_sender=True)
    else:
        flag = False
        for i in wife_lists.all_user:
            if i.id == send_user and i.fuckingBoy >= 20:
                await session.send(message="你抛弃了超过20位女孩，你不配活着，去死吧渣男", at_sender=True)
                return
            elif i.id == send_user:
                flag = True
                break
        if not flag:
            wife_lists.all_user.append(user(send_user))
        tempWife = wife(send_user)
        await  wife_lists.add_user(tempWife)
        await session.send(message=f"你好！我是{tempWife.name},从今天开始就成为你的妻子了，请多关照", at_sender=True)
    await write(wife_lists)
    return


def searchWife(session):
    msg = session.msg_text
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    send_user = session.event['user_id']
    for i in wife_lists.user_wife_list:
        if (None != re.search(i.name, msg)) and send_user == i.husband:
            print("执行！")
            a = love(session)
            loop.run_until_complete(a)
        elif i.name == msg:
            session.send(f"{i.name}:爪巴")
    else:
        pass


@sv.on_command('wife_index', aliases='老婆的个人信息', only_to_me=False)
async def wife_self_index(session: NLPSession):
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                await session.send(message=i.print_wife_index(), at_sender=True)
                return
    else:
        await session.send(message="你还没有老婆", at_sender=True)


@sv.on_command('end', aliases='分手', only_to_me=False)
async def love(session: NLPSession):
    send_user = session.event['user_id']
    for i in wife_lists.all_user:
        if i.id == send_user:
            i.fuckingBoy += 1
            break
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                if i.Character == '病娇':
                    await session.send(message=i.name + ":" + "这样啊……你不喜欢我么？那就杀死吧！ 没关系，只要在身边就可以了，无论以什么形式都可以；活着也好， "
                                                              "死掉也好，都可以。", at_sender=True)
                elif i.Character == '温柔':
                    await session.send(message=i.name + ":" + "这段时间感谢你照顾了，以后要好好吃饭，不要再熬夜了，请一定照顾好自己……", at_sender=True)
                elif i.Character == '傲娇':
                    await session.send(message=i.name + ":" + "哼，分就分，大笨蛋，我也从来就没有喜欢过你，就此别过吧……我绝对不会再想起你的，哼~永别了，八~嘎",
                                       at_sender=True)
                elif i.Character == '傲慢':
                    await session.send(message=i.name + ":" + "呵，愚蠢的人类，我以前居然对你这种似人非人的生物抱有爱慕，我真是愚蠢，那么祝你下地狱吧",
                                       at_sender=True)
                elif i.Character == '天真':
                    await session.send(message=i.name + ":" + "明明是我先来的~为什么……为什么你连分手都会这么熟练啊，为什么，我不懂啊！",
                                       at_sender=True)
                elif i.Character == '丧女':
                    await session.send(message=i.name + ":" + "啊……也是呢，我不会说话，长得也不漂亮，也不会打扮，还整天给你添乱，"
                                                              "各种方面来看我都是一个一无是处的废物呢，我这种人只会招人讨厌，不如死掉好了（笑），再见了",
                                       at_sender=True)
                elif i.Character == '腹黑':
                    await session.send(message=i.name + ":" + "（手后背刀）这样啊……那祝你幸福，永远找不到完整的女朋友哦",
                                       at_sender=True)
                elif i.Character == '蠢萌':
                    await session.send(message=i.name + ":" + "哎？你要分手吗？为什么啊QAQ？我哪里做得不好吗，我可以改，不要丢下我好不好QWQ",
                                       at_sender=True)
                elif i.Character == 'M':
                    await session.send(message=i.name + ":" + "啊……就是这样，请更多地鞭策我，你越是鞭策，我就越是喜欢你~尽管你这么说了，但我是绝对不会放弃你的",
                                       at_sender=True)
                elif i.Character == 'S':
                    await session.send(message=i.name + ":" + "切~看来你需要被我用高跟鞋踩在头上好好地调教一番呢",
                                       at_sender=True)
                elif i.Character == '弱气':
                    await session.send(message=i.name + ":" + "是这样吗……那以后还能做朋友吗……我还能见到你吗",
                                       at_sender=True)
                elif i.Character == '冒失':
                    await session.send(message=i.name + ":" + "分手？那是什么？能吃吗？啥？你要永远离开我了？不要啊，那样我会饿死的QAQ",
                                       at_sender=True)
                elif i.Character == '中二病':
                    await session.send(message=i.name + ":" + "深居于永劫深渊的恶魔啊，吾以主神宙斯之名命令汝，前去控制那个男人，让他永远沦为吾之奴仆吧！",
                                       at_sender=True)
                elif i.Character == '三无':
                    await session.send(message=i.name + ":" + "哦",
                                       at_sender=True)
                else:
                    await session.send(message=i.name + ":" + "祝你幸福", at_sender=True)
                wife_lists.user_wife_list.remove(i)
                wife_lists.user.remove(send_user)
                await  write(wife_lists)
                return
    else:
        await session.send(message="你没有老婆,谈什么分手", at_sender=True)


@sv.on_command('wife_shit', aliases='老婆骂我', only_to_me=False)
async def wife_shit(session: NLPSession):
    send_user = session.event['user_id']
    url = 'https://v1.alapi.cn/api/soul'
    date = requests.get(url).json()['data']['title']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                await session.send(i.name + ':' + date, at_sender=True)
    else:
        await session.send(message="你没有老婆", at_sender=True)


@sv.on_command('get_merry', aliases='结婚', only_to_me=False)
async def love(session: NLPSession):
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                await session.send(message=i.name + ":" + i.get_merry(), at_sender=True)
    else:
        await session.send(message="你没有老婆,谈什么结婚", at_sender=True)


@sv.on_command('wife_love', aliases=('老婆！', '爱我', '爱你'), only_to_me=False)
async def love(session: NLPSession):
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                i.isTalk = True
                i.liking += 2
                if i.scence == None:
                    i.scence = await get_love_scence()
                await session.send(message=str(i.name) + ":" + str(i.scence), at_sender=True)
                i.scence = await get_love_scence()
    else:
        await session.send(message="你没有老婆", at_sender=True)
