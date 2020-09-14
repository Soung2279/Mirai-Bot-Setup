import os
import random
import re
import urllib
import requests

from nonebot import on_command
from nonebot.exceptions import CQHttpError

from hoshino import R, Service, priv
from hoshino.typing import CQEvent

from hoshino.util import FreqLimiter, DailyNumberLimiter

_max = 1
EXCEED_NOTICE = f'今天已经施展了{_max}次爆裂魔法哦~~~明天再使用爆裂魔法吧!'
_nlmt = DailyNumberLimiter(_max)

sv = Service('explosion', visible=True, manage_priv=priv.ADMIN, enable_on_default=True)

exo_switch = True
a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
i = '9'
j = '10'

text1 = f'比黑色更黑，比黑暗更暗的漆黑。\n在此寄托吾真红的金光吧\n觉醒之时的到来，荒谬教会的堕落章理\n成为无形的扭曲而显现吧\n起舞吧，起舞吧，起舞吧\n吾之力量本源之愿的崩坏\n无人可及的崩坏\n将天地万象焚烧殆尽\n自深渊降临吧\n这就是人类最强威力的攻击手段\n这就是。究极攻击魔法\n「Explosion」'
text2 = f'被光明笼罩的漆黑啊\n身披夜之衣的爆炎啊\n以红魔族之名，显现原始的崩坏吧\n于终焉王国之地，引渡力量根源之物啊\n在吾面前展现吧\n「Explosion」'
text3 = f'赤红之黑炎，万界之君王\n天地之火咆哮之时\n吾乃万象相应之理\n化作崩坏与破坏之别名\n业火的铁锤降临吾掌\n「Explosion」'
text4 = f'吾名惠惠\n红魔族第一的魔法师\n兼爆裂魔法的操纵者\n好好见识我的力量吧\n「Explosion」'
text5 = f'以吾真红之流动\n颠覆白色之世界\n「Explosion」'
text6 = f'被光明笼罩的漆黑\n藏于夜色中的爆炎\n其它的暂且不提\n说到爆裂魔法，我不想输给任何人\n上了\n吾之究极破坏魔法\n「Explosion」'
text7 = f'降临空蝉的反转之天楼\n赐予吾身的虚无之信任\n时机已到\n现在就从沉睡中醒来\n听从吾之狂气显现吧\n穿刺吧\n「Explosion」'
text8 = f'环绕于我的乖逸精灵\n深渊的血肉狂然咆哮\n现在，成为红色波动的一部分吧\n穿刺吧\n「Explosion」'
text9 = f'吾名惠惠\n乃至高全能的支配者\n受命于天之力之人\n到来吧，到来吧，火焰的军势\n回应吾之所求，显现你的力量吧\n「Explosion」'
text10 = f'我名为惠惠\n红魔族第一最强的魔法使\n因为那时候悠悠让我走上爆裂魔法的路\n才有了今天的我\n吹拂吧狂风\n冥想吧爆炎\n爆裂魔法是浪漫\n是将不可能变为可能\n最强的魔法\n「Explosion」'


@sv.on_fullmatch(('爆裂魔法', '爆烈魔法', '暴烈魔法', 'EXPLOSION'))
async def exosend(bot, ev):
    uid = ev['user_id']
    if not _nlmt.check(uid):
        await bot.send(ev, EXCEED_NOTICE, at_sender=True)
        return
    if exo_switch:
        r = random.choice([a, b, c, d, e, f, g, h, i, j])
        print(r)
        if r == '1':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵1.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text1)
        if r == '2':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵2.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text2)
        if r == '3':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵3.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text3)
        if r == '4':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵4.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text4)
        if r == '5':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵5.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text5)
        if r == '6':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵6.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text6)    
        if r == '7':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵7.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text7)
        if r == '8':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵8.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text8)
        if r == '9':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵9.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text9)
        if r == '10':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵10.mp3'
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text10)

@sv.on_fullmatch(('补魔'), only_to_me=True)
async def exexplo(bot, ev: CQEvent):
    uid = ev['user_id']
    _nlmt.reset(uid)
    await bot.send(ev, f"谢谢你的魔力！我感觉又可以来一发了呢~")













