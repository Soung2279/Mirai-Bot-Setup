import os
import re
import random

from nonebot import on_command
from hoshino.typing import CQEvent
from hoshino import util, R, priv
from hoshino.service import Service

#为每个单独的目录指定单独的路径变量#
kkl_folder = R.img('randomimg/ma/').path
maomao_folder = R.img('randomimg/maomao/').path
wennai_folder = R.img('randomimg/wennai/').path
zaobanai_folder = R.img('randomimg/zaobanai/').path
bqb_folder = R.img('randomimg/bqb/').path
#=======================#
sv = Service('rdimg', enable_on_default=False, visible=False, manage_priv=priv.ADMIN)

#为每个单独的角色启用对应的指令#
#可以更改变量名称#
#注意需要在代码行里也填写对应的路径#
'''范例
@sv.on_fullmatch(('指令1','指令2', '指令3'), only_to_me=False)
async def 任意变量名(bot, ev):
    filelist = os.listdir(路径变量)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(路径变量, filename)
    pic = R.img('目录', filename).cqcode
    await bot.send(ev, pic, at_sender=False)
    '''

@sv.on_fullmatch(('来点可可萝', '来点kkl', '来点妈', '来点可可罗', '来点KKL'), only_to_me=False)
async def random_kkl(bot, ev):
    filelist = os.listdir(kkl_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kkl_folder, filename)
    pic = R.img('randomimg/ma/', filename).cqcode
    await bot.send(ev, pic, at_sender=False)

@sv.on_fullmatch(('来点猫猫头', '来点臭鼬', '来点黑猫', '来点凯留', '来点凯露'), only_to_me=False)
async def random_maomao(bot, ev):
    filelist = os.listdir(maomao_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(maomao_folder, filename)
    pic = R.img('randomimg/maomao/', filename).cqcode
    await bot.send(ev, pic, at_sender=False)
    
@sv.on_fullmatch(('来点早坂爱', '来点早坂'), only_to_me=False)
async def random_zaobanai(bot, ev):
    filelist = os.listdir(zaobanai_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(zaobanai_folder, filename)
    pic = R.img('randomimg/zaobanai/', filename).cqcode
    await bot.send(ev, pic, at_sender=False)    
    
@sv.on_fullmatch(('来点表情包','来点公会表情包', '来点pcr表情包', '来点PCR表情包'), only_to_me=False)
async def random_bqg(bot, ev):
    filelist = os.listdir(bqb_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(bqb_folder, filename)
    pic = R.img('randomimg/bqb/', filename).cqcode
    await bot.send(ev, pic, at_sender=False)