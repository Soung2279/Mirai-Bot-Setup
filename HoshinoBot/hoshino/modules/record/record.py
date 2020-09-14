import os, sys
import random

from random import choice
from hoshino.typing import CQEvent
from hoshino import R, Service, priv
from nonebot import MessageSegment

sv = Service('record', manage_priv=priv.ADMIN, visible=True, enable_on_default=True)

RECORD_HELP = '''
听游戏角色语音
[小仓唯语音] 听xcw老婆说话
[溴语音] 听水黑老婆说话
[🐱拳语音] 听猫拳老婆说话
支持角色原名，日文名，罗马音，呢称，别名，部分emoji
'''.strip()

@sv.on_fullmatch(('record帮助', 'record幫助'))
async def flac_help(bot, ev: CQEvent):
        await bot.send(ev, RECORD_HELP)

#   - 模板 -   #
'''
示范_folder = "F:/Resources/record/示范/"
@sv.on_fullmatch((
    "示范",
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(示范_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(示范_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
'''
#=========================#
hiyori_folder = "F:/Resources/record/100111猫拳/"
@sv.on_fullmatch((
    "猫拳语音", "日和语音", "ヒヨリ语音", "Hiyori语音", "日和莉语音", "🐱👊语音", "🐱拳语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(hiyori_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(hiyori_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
yui_folder = "F:/Resources/record/100211优衣/"
@sv.on_fullmatch((
    "优衣语音", "ユイ语音", "Yui语音", "种田语音", "普田语音", "由衣语音", "结衣语音", "ue语音", "↗↘↗↘语音", "yui语音", "由依语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(yui_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(yui_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
rei_folder = "F:/Resources/record/100311剑圣/"
@sv.on_fullmatch((
    "怜语音", "レイ语音", "Rei语音", "普怜语音", "伶语音", "rei语音", "剑圣语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(rei_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(rei_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
misogi_folder = "F:/Resources/record/100411炸弹/"
@sv.on_fullmatch((
    "禊语音", "ミソギ语音", "Misogi语音", "未奏希语音", "炸弹人语音", "💣语音", "炸弹语音", "misogi语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(misogi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(misogi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
matsuri_folder = "F:/Resources/record/100511跳跳虎/"
@sv.on_fullmatch((
    "茉莉语音", "マツリ语音", "Matsuri语音", "老虎语音", "虎语音", "🐅语音", "matsuri语音", "跳跳虎语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(matsuri_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(matsuri_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
akari_folder = "F:/Resources/record/100611妹法/"
@sv.on_fullmatch((
    "茜里语音", "アカリ语音", "Akari语音", "妹妹法语音", "妹法语音", "akari语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(akari_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(akari_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
miyako_folder = "F:/Resources/record/100711布丁/"
@sv.on_fullmatch((
    "宫子语音", "ミヤコ语音", "Miyako语音", "🍮语音", "布丁语音", "miyako语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(miyako_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(miyako_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
yuki_folder = "F:/Resources/record/100811镜子/"
@sv.on_fullmatch((
    "雪语音", "ユキ语音", "Yuki语音", "雪哥语音", "镜法语音", "伪娘语音", "男孩子语音", "男孩纸语音", "yuki语音", "镜子语音", "男公主语音", "♂公主语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(yuki_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(yuki_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
anna_folder = "F:/Resources/record/100911中二/"
@sv.on_fullmatch((
    "杏奈语音", "アンナ语音", "Anna语音", "煤气罐语音", "anna语音", "自爆罐语音", "自爆怪语音", "中二语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(anna_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(anna_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
maho_folder = "F:/Resources/record/101011狐狸/"
@sv.on_fullmatch((
    "真步语音", "マホ语音", "Maho语音", "真扎语音", "咕噜灵波语音", "真布语音", "🦊语音", "maho语音", "狐狸语音", "咕噜凌波语音", "咕噜绫波语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(maho_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(maho_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
rino_folder = "F:/Resources/record/101111妹弓/"
@sv.on_fullmatch((
    "璃乃语音", "リノ语音", "Rino语音", "rino语音", "妹弓语音", "妹妹弓语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(rino_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(rino_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
hatsune_folder = "F:/Resources/record/101211初音/"
@sv.on_fullmatch((
    "ハツネ语音", "Hatsune语音", "hego语音", "星法语音", "星星法语音", "⭐法语音", "睡法语音", "hatsune语音", "初音语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(hatsune_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(hatsune_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
nanaka_folder = "F:/Resources/record/101311七七香/"
@sv.on_fullmatch((
    "ナナカ语音", "Nanaka语音", "娜娜卡语音", "77k语音", "77香语音", "七七香语音", "nanaka语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(nanaka_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(nanaka_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kasumi_folder = "F:/Resources/record/101411侦探/"
@sv.on_fullmatch((
    "霞语音", "カスミ语音", "Kasumi语音", "香澄语音", "杜宾犬语音", "驴语音", "驴子语音", "🔍语音", "kasumi语音", "侦探语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kasumi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kasumi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
misato_folder = "F:/Resources/record/101511圣母/"
@sv.on_fullmatch((
    "美里语音", "ミサト语音", "Misato语音", "圣女语音", "圣母语音", "misato语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(misato_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(misato_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
suzuna_folder = "F:/Resources/record/101611暴击弓/"
@sv.on_fullmatch((
    "铃奈语音", "スズナ语音", "Suzuna语音", "暴弓语音", "爆击弓语音", "爆弓语音", "政委语音", "suzuna语音", "暴击弓语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(suzuna_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(suzuna_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kaori_folder = "F:/Resources/record/101711狗拳/"
@sv.on_fullmatch((
    "香织语音", "カオリ语音", "Kaori语音", "琉球犬语音", "狗子语音", "狗语音", "🐶语音", "🐕语音", "🐶👊🏻语音", "🐶👊语音", "狗拳语音", "kaori语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kaori_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kaori_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
io_folder = "F:/Resources/record/101811老师/"
@sv.on_fullmatch((
    "伊绪语音", "イオ语音", "Io语音", "魅魔语音", "io语音", "老师语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(io_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(io_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
mimi_folder = "F:/Resources/record/102011兔子/"
@sv.on_fullmatch((
    "美美语音", "ミミ语音", "Mimi语音", "兔兔语音", "萝卜霸断剑语音", "人参霸断剑语音", "天兔霸断剑语音", "🐇语音", "🐰语音", "mimi语音", "兔子语音", "兔剑语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(mimi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(mimi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kurumi_folder = "F:/Resources/record/102111铃铛/"
@sv.on_fullmatch((
    "胡桃语音", "クルミ语音", "Kurumi语音", "🔔语音", "kurumi语音", "铃铛语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kurumi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kurumi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
yori_folder = "F:/Resources/record/102211姐法/"
@sv.on_fullmatch((
    "依里语音", "ヨリ语音", "Yori语音", "姐姐法语音", "姐法语音", "yori语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(yori_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(yori_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ayane_folder = "F:/Resources/record/102311熊锤/"
@sv.on_fullmatch((
    "绫音语音", "アヤネ语音", "Ayane语音", "🐻🔨语音", "🐻语音", "熊锤语音", "ayane语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ayane_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ayane_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
suzume_folder = "F:/Resources/record/102511女仆/"
@sv.on_fullmatch((
    "铃莓语音", "スズメ语音", "Suzume语音", "妹抖语音", "suzume语音", "女仆语音", "maid语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(suzume_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(suzume_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
rin_folder = "F:/Resources/record/102611松鼠/"
@sv.on_fullmatch((
    "铃语音", "リン语音", "Rin语音", "🐿语音", "🐿️语音", "松鼠语音", "rin语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(rino_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(rino_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
eriko_folder = "F:/Resources/record/102711病娇/"
@sv.on_fullmatch((
    "惠理子语音", "エリコ语音", "Eriko语音", "eriko语音", "病娇语音", "惠里子语音", "绘里子语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(eriko_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(eriko_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
saren_folder = "F:/Resources/record/102811充电宝/"
@sv.on_fullmatch((
    "咲恋语音", "サレン语音", "Saren语音", "青梅竹马语音", "幼驯染语音", "院长语音", "园长语音", "🔋语音", "充电宝语音", "saren语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(saren_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(saren_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
nozomi_folder = "F:/Resources/record/102911偶像/"
@sv.on_fullmatch((
    "望语音", "ノゾミ语音", "Nozomi语音", "小望语音", "🎤语音", "偶像语音", "樱井望语音", "nozomi语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(nozomi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(nozomi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ninon_folder = "F:/Resources/record/103011扇子/"
@sv.on_fullmatch((
    "妮诺语音", "ニノン语音", "Ninon语音", "妮侬语音", "扇子语音", "ninon语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ninon_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ninon_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shinobu_folder = "F:/Resources/record/103111忍/"
@sv.on_fullmatch((
    "シノブ语音", "Shinobu语音", "普忍语音", "鬼父语音", "💀语音", "忍语音", "shinobu语音", "骷髅语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shinobu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shinobu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
akino_folder = "F:/Resources/record/103211哈哈剑/"
@sv.on_fullmatch((
    "秋乃语音", "アキノ语音", "Akino语音", "akino语音", "哈哈剑语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(akino_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(akino_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
mahiru_folder = "F:/Resources/record/103311奶牛/"
@sv.on_fullmatch((
    "真阳语音", "マヒル语音", "Mahiru语音", "🐄语音", "🐮语音", "真☀语音", "mahiru语音", "奶牛语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(mahiru_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(mahiru_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
yukari_folder = "F:/Resources/record/103411黄骑/"
@sv.on_fullmatch((
    "优花梨语音", "ユカリ语音", "Yukari语音", "由加莉语音", "酒鬼语音", "奶骑语音", "圣骑语音", "🍺语音", "🍺👻语音", "yukari语音", "黄骑语音", "由嘉莉语音", "由加利语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(yukari_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(yukari_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kyouka_folder = "F:/Resources/record/103611小仓唯/"
@sv.on_fullmatch((
    "镜华语音", "キョウカ语音", "Kyouka语音", "xcw语音", "小苍唯语音", "8岁语音", "八岁语音", "喷水萝语音", "八岁喷水萝语音", "8岁喷水萝语音", "XCW语音", "kyouka语音", "小仓唯语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kyouka_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kyouka_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
tomo_folder = "F:/Resources/record/103711卜毛/"
@sv.on_fullmatch((
    "智语音", "トモ语音", "Tomo语音", "卜毛语音", "tomo语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(tomo_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(tomo_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shiori_folder = "F:/Resources/record/103811tp弓/"
@sv.on_fullmatch((
    "栞语音", "シオリ语音", "Shiori语音", "TP弓语音", "小栞语音", "白虎弓语音", "白虎妹语音", "tp弓语音", "shiori语音", "病弱语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shiori_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shiori_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
aoi_folder = "F:/Resources/record/104011香菜弓/"
@sv.on_fullmatch((
    "碧语音", "アオイ语音", "Aoi语音", "香菜语音", "绿毛弓语音", "毒弓语音", "绿帽弓语音", "绿帽语音", "aoi语音", "香菜弓语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(aoi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(aoi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
chika_folder = "F:/Resources/record/104211绿毛/"
@sv.on_fullmatch((
    "チカ语音", "Chika语音", "绿毛奶语音", "千歌语音", "绿毛语音", "chika语音" , "千歌奶语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(chika_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(chika_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
makoto_folder = "F:/Resources/record/104311狼/"
@sv.on_fullmatch((
    "真琴语音", "マコト语音", "Makoto语音", "🐺语音", "月月语音", "朋语音", "狼语音", "普狼语音", "makoto语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(makoto_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(makoto_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
iriya_folder = "F:/Resources/record/104411伊利亚/"
@sv.on_fullmatch((
    "伊莉亚语音", "イリヤ语音", "Iriya语音", "伊莉雅语音", "伊利雅语音", "yly语音", "吸血鬼语音", "那个女人语音", "伊利亚语音", "iriya语音", "YLY语音", "辣个女人语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(iriya_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(iriya_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kuuka_folder = "F:/Resources/record/104511抖m/"
@sv.on_fullmatch((
    "空花语音", "クウカ语音", "Kuuka语音", "抖m语音", "kuuka语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kuuka_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kuuka_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
tamaki_folder = "F:/Resources/record/104611猫剑/"
@sv.on_fullmatch((
    "珠希语音", "タマキ语音", "Tamaki语音", "🐱剑语音", "🐱🗡️语音", "猫剑语音", "tamaki语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(tamaki_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(tamaki_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
jun_folder = "F:/Resources/record/104711黑骑/"
@sv.on_fullmatch((
    "纯语音", "ジュン语音", "Jun语音", "saber语音", "SABER语音", "黑骑语音", "jun语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(jun_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(jun_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
mifuyu_folder = "F:/Resources/record/104811子龙/"
@sv.on_fullmatch((
    "美冬语音", "ミフユ语音", "Mifuyu语音", "赵子龙语音", "子龙语音", "mifuyu语音", "美东语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(mifuyu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(mifuyu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shizuru_folder = "F:/Resources/record/104911姐姐/"
@sv.on_fullmatch((
    "静流语音", "シズル语音", "Shizuru语音", "shizuru语音", "姐姐语音", "大姐姐语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shizuru_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shizuru_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
misaki_folder = "F:/Resources/record/105011大眼/"
@sv.on_fullmatch((
    "美咲语音", "ミサキ语音", "Misaki语音", "👀语音", "👁️语音", "👁语音", "大眼语音", "misaki语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(misaki_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(misaki_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
mitsuki_folder = "F:/Resources/record/105111深月/"
@sv.on_fullmatch((
    "ミツキ语音", "Mitsuki语音", "眼罩语音", "抖s语音", "mitsuki语音", "深月语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(mitsuki_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(mitsuki_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
rima_folder = "F:/Resources/record/105211羊驼/"
@sv.on_fullmatch((
    "莉玛语音", "リマ语音", "Rima语音", "Lima语音", "草泥马语音", "🦙语音", "🐐语音", "羊驼语音", "rima语音", "lima语音", "莉马语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(rima_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(rima_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
monika_folder = "F:/Resources/record/105311毛二力/"
@sv.on_fullmatch((
    "毛二力语音", "莫妮卡语音", "モニカ语音", "Monika语音", "monika语音", "莫尼卡语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(monika_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(monika_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
tsumugi_folder = "F:/Resources/record/105411裁缝/"
@sv.on_fullmatch((
    "纺希语音", "ツムギ语音", "Tsumugi语音", "蜘蛛侠语音", "🕷️语音", "🕸️语音", "裁缝语音", "tsumugi语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(tsumugi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(tsumugi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ayumi_folder = "F:/Resources/record/105511路人/"
@sv.on_fullmatch((
    "步未语音", "アユミ语音", "Ayumi语音", "步美语音", "路人妹语音", "路人语音", "ayumi语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ayumi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ayumi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ruka_folder = "F:/Resources/record/105611流夏/"
@sv.on_fullmatch((
    "ルカ语音", "Ruka语音", "大姐语音", "大姐头语音", "流夏语音", "ruka语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ruka_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ruka_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
jiita_folder = "F:/Resources/record/105711吉他/"
@sv.on_fullmatch((
    "吉塔语音", "ジータ语音", "Jiita语音", "姬塔语音", "团长语音", "🎸语音", "吉他语音", "骑空士语音", "qks语音", "古战场逃兵语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(jiita_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(jiita_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
pecoriinu_folder = "F:/Resources/record/105811佩可/"
@sv.on_fullmatch((
    "贪吃佩可语音", "ペコリーヌ语音", "Pecoriinu语音", "佩可莉姆语音", "吃货语音", "公主语音", "饭团语音", "🍙语音", "佩可语音", "pecoriinu语音", "尤丝蒂亚娜·F·阿斯特莱亚语音", "Eustiana von Astraea语音", "ユースティアナ・フォン・アストライア语音", "尤丝蒂亚娜语音", "eustiana语音", "Eustiana语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(pecoriinu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(pecoriinu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kokkoro_folder = "F:/Resources/record/105911妈/"
@sv.on_fullmatch((
    "kkl语音", "コッコロ语音", "Kokkoro语音", "可可罗语音", "妈语音", "普白语音", "可可萝语音", "kokkoro语音", "KKL语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kokkoro_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kokkoro_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kyaru_folder = "F:/Resources/record/106011黑猫/"
@sv.on_fullmatch((
    "凯留语音", "キャル语音", "Kyaru语音", "凯露语音", "希留耶语音", "Kiruya语音", "臭鼬语音", "普黑语音", "黑猫语音", "kyaru语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kyaru_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kyaru_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
muimi_folder = "F:/Resources/record/106111无意义/"
@sv.on_fullmatch((
    "矛依未语音", "ムイミ语音", "Muimi语音", "诺维姆语音", "Noemu语音", "夏娜语音", "无意义语音", "天楼霸断剑语音", "511语音", "muimi语音", "noemu语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(muimi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(muimi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
arisa_folder = "F:/Resources/record/106311亚里沙/"
@sv.on_fullmatch((
    "亚里莎语音", "アリサ语音", "Arisa语音", "鸭梨瞎语音", "瞎子语音", "鸭梨傻语音", "亚丽莎语音", "亚莉莎语音", "瞎子弓语音", "🍐🦐语音", "亚里沙语音", "arisa语音", "yls语音", "YLS语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(arisa_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(arisa_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kaya_folder = "F:/Resources/record/106511嘉夜/"
@sv.on_fullmatch((
    "カヤ语音", "Kaya语音", "憨憨龙语音", "🐲👊🏻语音", "🐉👊🏻语音", "嘉夜语音", "嘉业语音", "kaya语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kaya_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kaya_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
neneka_folder = "F:/Resources/record/107011nnk/"
@sv.on_fullmatch((
    "似似花语音", "ネネカ语音", "Neneka语音", "变貌大妃语音", "448语音", "捏捏卡语音", "变貌语音", "大妃语音", "nnk语音", "neneka语音", "NNK语音", "永远地神语音", "永远滴神语音", "永远嘀神语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(neneka_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(neneka_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
christina_folder = "F:/Resources/record/107111克总/"
@sv.on_fullmatch((
    "克莉丝提娜语音", "クリスティーナ语音", "Kurisutiina语音", "Christina语音", "Cristina语音", "誓约女君语音", "女帝语音", "克语音", "克总语音", "kurisutiina语音", "christina语音", "cristina语音", "誓约女帝语音", "克里斯提娜语音", "克里斯汀娜语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(christina_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(christina_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuichi_folder = "F:/Resources/record/107511水吃/"
@sv.on_fullmatch((
    "贪吃佩可(夏日)语音", "ペコリーヌ(サマー)语音", "Pekoriinu(Summer)语音", "水饭语音", "水吃货语音", "水佩可语音", "水公主语音", "水饭团语音", "水🍙语音", "泳吃语音", "泳饭语音", "泳吃货语音", "泳佩可语音", "泳公主语音", "泳饭团语音", "泳🍙语音", "泳装吃货语音", "泳装公主语音", "泳装饭团语音", "泳装🍙语音", "佩可(夏日)语音", "🥡语音", "👙🍙语音", "泼妇语音", "水吃语音", "pekoriinu(summer)语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuichi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuichi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuima_folder = "F:/Resources/record/107611水妈/"
@sv.on_fullmatch((
    "可可萝(夏日)语音", "コッコロ(サマー)语音", "Kokkoro(Summer)语音", "水白语音", "水可语音", "水可可语音", "水可可萝语音", "水可可罗语音", "泳装可可萝语音", "泳装可可罗语音", "水妈语音", "氵妈语音", "氵白语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuima_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuima_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuinvpu_folder = "F:/Resources/record/107711水女仆/"
@sv.on_fullmatch((
    "铃莓(夏日)语音", "スズメ(サマー)语音", "Suzume(Summer)语音", "水妹抖语音", "水女仆语音", "水maid语音", "氵女仆语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuinvpu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuinvpu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuihei_folder = "F:/Resources/record/107811水黑/"
@sv.on_fullmatch((
    "凯留(夏日)语音", "キャル(サマー)语音", "Kyaru(Summer)语音", "水黑语音", "水黑猫语音", "水臭鼬语音", "泳装黑猫语音", "泳装臭鼬语音", "潶语音", "溴语音", "💧黑语音", "氵黑语音", "氵黑猫语音", "法狼语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuihei_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuihei_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuimaojian_folder = "F:/Resources/record/107911水猫剑/"
@sv.on_fullmatch((
    "珠希(夏日)语音", "タマキ(サマー)语音", "Tamaki(Summer)语音", "水猫语音", "渵语音", "💧🐱🗡️语音", "水🐱🗡️语音", "水猫剑语音", "氵猫剑语音", "氵猫语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuimaojian_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuimaojian_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuizilong_folder = "F:/Resources/record/108011水子龙/"
@sv.on_fullmatch((
    "美冬(夏日)语音", "ミフユ(サマー)语音", "Mifuyu(Summer)语音", "水美冬语音", "水子龙语音", "氵子龙语音", "氵美冬语音", "水美东语音", "氵美东语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuizilong_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuizilong_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
wanshengren_folder = "F:/Resources/record/108111万圣忍/"
@sv.on_fullmatch((
    "忍(万圣节)语音", "シノブ(ハロウィン)语音", "Shinobu(Halloween)语音", "瓜忍语音", "🎃忍语音", "🎃💀语音", "万圣忍语音", "万圣骷髅语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(wanshengren_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(wanshengren_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
wanshengdayan_folder = "F:/Resources/record/108311万圣大眼/"
@sv.on_fullmatch((
    "美咲(万圣节)语音", "ミサキ(ハロウィン)语音", "Misaki(Halloween)语音", "万圣美咲语音", "瓜眼语音", "🎃眼语音", "🎃👀语音", "🎃👁️语音", "🎃👁语音", "万圣大眼语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(wanshengdayan_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(wanshengdayan_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
wanshengbuding_folder = "F:/Resources/record/108211万圣布丁/"
@sv.on_fullmatch((
    "宫子(万圣节)语音", "ミヤコ(ハロウィン)语音", "Miyako(Halloween)语音", "万圣宫子语音", "狼丁语音", "狼布丁语音", "万圣🍮语音", "🐺🍮语音", "🎃🍮语音", "👻🍮语音", "万圣布丁语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(wanshengbuding_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(wanshengbuding_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shengdanqiange_folder = "F:/Resources/record/108411圣诞千歌/"
@sv.on_fullmatch((
    "千歌(圣诞节)语音", "チカ(クリスマス)语音", "Chika(Xmas)语音", "圣千语音", "蛋鸽语音", "🎄💰🎶语音", "🎄千🎶语音", "🎄1000🎶语音", "圣诞千歌语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shengdanqiange_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shengdanqiange_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shengdanlingdang_folder = "F:/Resources/record/108511圣诞铃铛/"
@sv.on_fullmatch((
    "胡桃(圣诞节)语音", "クルミ(クリスマス)语音", "Kurumi(Xmas)语音", "圣诞胡桃语音", "圣诞铃铛语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shengdanlingdang_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shengdanlingdang_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shengdanxiongchui_folder = "F:/Resources/record/108611圣诞熊锤/"
@sv.on_fullmatch((
    "绫音(圣诞节)语音", "アヤネ(クリスマス)语音", "Ayane(Xmas)语音", "蛋锤语音", "圣锤语音", "🎄🐻🔨语音", "🎄🐻语音", "圣诞熊锤语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shengdanxiongchui_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shengdanxiongchui_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
xinchunmaoquan_folder = "F:/Resources/record/108711新春猫拳/"
@sv.on_fullmatch((
    "日和(新年)语音", "ヒヨリ(ニューイヤー)语音", "Hiyori(NewYear)语音", "新年日和语音", "春猫语音", "👘🐱语音", "新春猫拳语音", "春猫拳语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(xinchunmaoquan_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(xinchunmaoquan_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
chuntian_folder = "F:/Resources/record/108811春田/"
@sv.on_fullmatch((
    "优衣(新年)语音", "ユイ(ニューイヤー)语音", "Yui(NewYear)语音", "新年优衣语音", "新年由衣语音", "春田语音", "新春由依语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(chuntian_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(chuntian_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
xinchunjiansheng_folder = "F:/Resources/record/108911新春剑圣/"
@sv.on_fullmatch((
    "怜(新年)语音", "レイ(ニューイヤー)语音", "Rei(NewYear)语音", "春剑语音", "春怜语音", "春伶语音", "新春剑圣语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(xinchunjiansheng_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(xinchunjiansheng_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
lianbing_folder = "F:/Resources/record/109011情人节病娇/"
@sv.on_fullmatch((
    "惠理子(情人节)语音", "エリコ(バレンタイン)语音", "Eriko(Valentine)语音", "恋病语音", "情病语音", "恋病娇语音", "情病娇语音", "情人节病娇语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(lianbing_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(lianbing_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
qingrenjiejiejie_folder = "F:/Resources/record/109111情人节姐姐/"
@sv.on_fullmatch((
    "静流(情人节)语音", "シズル(バレンタイン)语音", "Shizuru(Valentine)语音" "情人节静流语音", "情姐语音", "情人节姐姐语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(qingrenjiejiejie_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(qingrenjiejiejie_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
an_folder = "F:/Resources/record/109211安/"
@sv.on_fullmatch((
    "アン语音", "An语音", "胖安语音", "55kg语音", "安语音", "an语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(an_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(an_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ruu_folder = "F:/Resources/record/109311眼球/"
@sv.on_fullmatch((
    "露语音", "ルゥ语音", "Ruu语音", "逃课女王语音", "ruu语音", "逃课语音", "眼球语音", "眼球法语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ruu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ruu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
gurea_folder = "F:/Resources/record/109411龙姬/"
@sv.on_fullmatch((
    "古蕾娅语音", "グレア语音", "Gurea语音", "古雷娅语音", "古蕾亚语音", "古雷亚语音", "🐲🐔语音", "🐉🐔语音", "龙姬语音", "gurea语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(gurea_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(gurea_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
jianghushanzi_folder = "F:/Resources/record/109611江户扇子/"
@sv.on_fullmatch((
    "妮诺(大江户)语音", "ニノン(オーエド)语音", "Ninon(Ooedo)语音", "江户扇子语音", "忍扇语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(jianghushanzi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(jianghushanzi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
jianghum_folder = "F:/Resources/record/109511江户抖m/"
@sv.on_fullmatch((
    "空花(大江户)语音", "クウカ(オーエド)语音", "Kuuka(Ooedo)语音", "江户空花语音", "江m语音", "花m语音", "江花语音", "江户抖m", "江户抖M"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(jianghum_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(jianghum_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
remu_folder = "F:/Resources/record/109711蕾姆/"
@sv.on_fullmatch((
    "雷姆语音", "レム语音", "Remu语音", "蕾姆语音", "remu语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(remu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(remu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ramu_folder = "F:/Resources/record/109811拉姆/"
@sv.on_fullmatch((
    "ラム语音", "Ramu语音", "拉姆语音", "ramu语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ramu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ramu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
emiria_folder = "F:/Resources/record/109911艾米莉亚/"
@sv.on_fullmatch((
    "爱蜜莉雅语音", "エミリア语音", "Emiria语音", "艾米莉亚语音", "emt语音", "EMT语音", "艾米利亚语音", "艾米丽亚语音", "艾米丽雅语音", "emiria语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(emiria_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(emiria_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuibao_folder = "F:/Resources/record/110011水暴/"
@sv.on_fullmatch((
    "铃奈(夏日)语音", "スズナ(サマー)语音", "Suzuna(Summer)语音", "瀑击弓语音", "水爆语音", "水爆弓语音", "瀑语音", "水暴弓语音", "瀑弓语音", "泳装暴弓语音", "泳装爆弓语音", "水暴语音", "氵爆语音", "氵暴语音", "氵政委语音", "水政委语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuibao_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuibao_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuilaoshi_folder = "F:/Resources/record/110111水老师/"
@sv.on_fullmatch((
    "伊绪(夏日)语音", "イオ(サマー)语音", "Io(Summer)语音", "水魅魔语音", "泳装魅魔语音", "泳装老师语音", "水老师语音", "氵老师语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuilaoshi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuilaoshi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuidianzhan_folder = "F:/Resources/record/110311水电站/"
@sv.on_fullmatch((
    "咲恋(夏日)语音", "サレン(サマー)语音", "Saren(Summer)语音", "水电语音", "泳装充电宝语音", "泳装咲恋语音", "水着咲恋语音", "水电宝语音", "水充语音", "👙🔋语音", "水电站语音", "充电的神语音", "充电滴神语音", "充电地神语音", "充电嘀神语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuidianzhan_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuidianzhan_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuilang_folder = "F:/Resources/record/110411水狼/"
@sv.on_fullmatch((
    "真琴(夏日)语音", "マコト(サマー)语音", "Makoto(Summer)语音", "浪语音", "水🐺语音", "泳狼语音", "泳月语音", "泳月月语音", "泳朋语音", "水月语音", "水月月语音", "水朋语音", "👙🐺语音", "水狼语音", "氵狼语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuilang_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuilang_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuigou_folder = "F:/Resources/record/110511水狗/"
@sv.on_fullmatch((
    "香织(夏日)语音", "カオリ(サマー)语音", "Kaori(Summer)语音", "泃语音", "水🐶语音", "水🐕语音", "泳狗语音", "水狗语音", "氵狗语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuigou_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuigou_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuihuli_folder = "F:/Resources/record/110611水狐狸/"
@sv.on_fullmatch((
    "真步(夏日)语音", "マホ(サマー)语音", "Maho(Summer)语音", "水壶语音", "水真步语音", "水maho语音", "氵🦊语音", "水🦊语音", "💧🦊语音", "氵狐狸语音", "水狐狸语音", "水真布语音", "氵真布语音", "氵狐语音", "水狐语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuihuli_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuihuli_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
jkxiangcai_folder = "F:/Resources/record/110711jk香菜/"
@sv.on_fullmatch((
    "碧(插班生)语音", "アオイ(編入生)语音", "Aoi(Hennyuusei)语音", "生菜语音", "jk香菜语音", "JK香菜语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(jkxiangcai_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(jkxiangcai_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
kuroe_folder = "F:/Resources/record/110811华哥/"
@sv.on_fullmatch((
    "克萝依语音", "クロエ语音", "Kuroe语音", "黑江语音", "华哥语音", "kuroe语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(kuroe_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(kuroe_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
chieru_folder = "F:/Resources/record/110911切噜/"
@sv.on_fullmatch((
    "琪爱儿语音", "チエル语音", "Chieru语音", "切露语音", "茄露语音", "茄噜语音", "chieru语音", "切噜语音", "切噜噜语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(chieru_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(chieru_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
yuni_folder = "F:/Resources/record/111011优妮/"
@sv.on_fullmatch((
    "ユニ语音", "Yuni语音", "u2语音", "优妮辈先语音", "辈先语音", "书记语音", "优妮语音", "yuni语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(yuni_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(yuni_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
maocangwei_folder = "F:/Resources/record/111111猫仓唯/"
@sv.on_fullmatch((
    "镜华(万圣节)语音", "キョウカ(ハロウィン)语音", "Kyouka(Halloween)语音", "万圣镜华语音", "万圣小仓唯语音", "万圣xcw语音", "黑猫仓唯语音", "mcw语音", "猫唯语音", "猫仓语音", "喵唯语音", "猫仓唯语音", "MCW语音", "猫苍唯语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(maocangwei_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(maocangwei_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
wanshengzhadan_folder = "F:/Resources/record/111211万圣炸弹/"
@sv.on_fullmatch((
    "禊(万圣节)语音", "ミソギ(ハロウィン)语音", "Misogi(Halloween)语音", "万圣禊语音", "万圣炸弹人语音", "瓜炸弹人语音", "万圣炸语音", "瓜炸语音", "南瓜炸语音", "🎃💣语音", "万圣炸弹语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(wanshengzhadan_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(wanshengzhadan_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
wanshengtuzi_folder = "F:/Resources/record/111311万圣兔子/"
@sv.on_fullmatch((
    "美美(万圣节)语音", "ミミ(ハロウィン)语音", "Mimi(Halloween)", "万圣兔语音", "万圣兔兔语音", "绷带兔语音", "绷带兔子语音", "万圣美美语音", "绷带美美语音", "万圣🐰语音", "绷带🐰语音", "🎃🐰语音", "万圣🐇语音", "绷带🐇语音", "🎃🐇语音", "万圣兔子语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(wanshengtuzi_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(wanshengtuzi_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
runa_folder = "F:/Resources/record/111411露娜/"
@sv.on_fullmatch((
    "ルナ语音", "Runa语音", "露仓唯语音", "露cw语音", "luna语音", "runa语音", "露娜语音", "Luna语音", "露苍唯语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(runa_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(runa_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shengdanke_folder = "F:/Resources/record/111511圣诞克总/"
@sv.on_fullmatch((
    "克莉丝提娜(圣诞节)语音", "クリスティーナ(クリスマス)语音", "Kurisutiina(Xmas)语音", "Christina(Xmas)语音", "Cristina(Xmas)语音", "圣诞克语音", "圣诞女帝语音", "蛋克语音", "圣克语音", "必胜客语音", "圣诞克总语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shengdanke_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shengdanke_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shengdanouxiang_folder = "F:/Resources/record/111611圣诞偶像/"
@sv.on_fullmatch((
    "望(圣诞节)语音", "ノゾミ(クリスマス)语音", "Nozomi(Xmas)语音", "圣诞望语音", "蛋偶像语音", "蛋望语音", "圣诞偶像语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shengdanouxiang_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shengdanouxiang_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shengdanyly_folder = "F:/Resources/record/111711圣诞伊利亚/"
@sv.on_fullmatch((
    "伊莉亚(圣诞节)语音", "イリヤ(クリスマス)语音", "Iriya(Xmas)语音", "圣诞伊莉亚语音", "圣诞伊莉雅语音", "圣诞伊利雅语音", "圣诞yly语音", "圣诞吸血鬼语音", "圣伊语音", "圣yly语音", "圣诞伊利亚语音", "圣诞YLY语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shengdanyly_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shengdanyly_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
chunma_folder = "F:/Resources/record/111911春妈/"
@sv.on_fullmatch((
    "可可萝(新年)语音", "コッコロ(ニューイヤー)语音", "Kokkoro(NewYear)语音", "春可可语音", "春白语音", "新年妈语音", "春妈语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(chunma_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(chunma_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
chunhei_folder = "F:/Resources/record/112011春黑/"
@sv.on_fullmatch((
    "凯留(新年)语音", "キャル(ニューイヤー)语音", "Kyaru(NewYear)语音", "春凯留语音", "春黑猫语音", "春臭鼬语音", "新年凯留语音", "新年黑猫语音", "新年臭鼬语音", "唯一神语音", "春黑语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(chunhei_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(chunhei_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
chunnvpu_folder = "F:/Resources/record/112111春女仆/"
@sv.on_fullmatch((
    "铃莓(新年)语音", "スズメ(ニューイヤー)语音", "Suzume(NewYear)语音", "春铃莓语音", "春妹抖语音", "新年铃莓语音", "新年女仆语音", "新年妹抖语音", "春女仆语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(chunnvpu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(chunnvpu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shaojiuxian_folder = "F:/Resources/record/112211魔法少女霞/"
@sv.on_fullmatch((
    "霞(魔法少女)语音", "カスミ(マジカル)语音", "Kasumi(MagiGirl)语音", "魔法侦探语音", "魔法杜宾犬语音", "魔法驴语音", "魔法驴子语音", "魔驴语音", "魔法霞语音", "魔法少驴语音", "魔法少女霞语音", "马猴烧酒霞语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shaojiuxian_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shaojiuxian_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shaojiukan_folder = "F:/Resources/record/112311魔法少女栞/"
@sv.on_fullmatch((
    "栞(魔法少女)语音", "シオリ(マジカル)语音", "Shiori(MagiGirl)语音", "魔法tp弓语音", "魔法TP弓语音", "魔法小栞语音", "魔法白虎弓语音", "魔法白虎妹语音", "魔法白虎语音", "魔法少女栞语音", "马猴烧酒栞语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shaojiukan_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shaojiukan_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
youqibingniu_folder = "F:/Resources/record/112811游骑兵奶牛/"
@sv.on_fullmatch((
    "真阳(游骑兵)语音", "マヒル(レンジャー)语音", "Mahiru(Ranger)语音", "骑兵奶牛语音", "游侠奶牛语音", "护林员奶牛语音", "护林奶牛语音", "游侠🐄语音", "游侠🐮语音", "游骑兵奶牛语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(youqibingniu_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(youqibingniu_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
shuanggong_folder = "F:/Resources/record/112911爽弓/"
@sv.on_fullmatch((
    "璃乃(奇境)语音", "リノ(ワンダー)语音", "Rino(Wonder)语音", "璃乃(仙境)语音", "爱丽丝弓语音", "爱弓语音", "兔弓语音", "奇境妹弓语音", "仙境妹弓语音", "白丝妹弓语音", "爽弓语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(shuanggong_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(shuanggong_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
ailisiluren_folder = "F:/Resources/record/113011爱丽丝路人/"
@sv.on_fullmatch((
    "步未(奇境)语音", "アユミ(ワンダー)语音", "Ayumi(Wonder)语音", "步未(仙境)语音", "路人兔语音", "兔人妹语音", "奇境路人语音", "仙境路人语音", "爱丽丝路人语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(ailisiluren_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(ailisiluren_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
gaoda_folder = "F:/Resources/record/180411高达吃货/"
@sv.on_fullmatch((
    "贪吃佩可(公主)语音", "ペコリーヌ(プリンセス)语音", "Pekoriinu(Princess)语音", "公主吃语音", "公主饭语音", "公主吃货语音", "公主佩可语音", "公主饭团语音", "公主🍙语音", "命运高达语音", "高达语音", "命运公主语音", "高达公主语音", "春哥高达语音", "🤖🍙语音", "🤖语音", "高达吃货语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(gaoda_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(gaoda_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
diema_folder = "F:/Resources/record/180511蝶妈/"
@sv.on_fullmatch((
    "可可萝(公主)语音", "コッコロ（プリンセス）语音", "Kokkoro(Princess)语音", "公主妈语音", "月光妈语音", "蝴蝶妈语音", "月光蝶妈语音", "公主可语音", "公主可萝语音", "公主可可萝语音", "月光可语音", "月光可萝语音", "月光可可萝语音", "蝶可语音", "蝶可萝语音", "蝶可可萝语音", "蝶妈语音"
    ), only_to_me=False)
async def record_send(bot, ev):
    filelist = os.listdir(diema_folder)
    path = None
    while not path or not os.path.isfile(path):
        filename = random.choice(filelist)
        path = os.path.join(diema_folder, filename)
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
#=========================#
#自检指令#
@sv.on_fullmatch(('record检查'), only_to_me=False)
async def test_check(bot, ev):
    await bot.send(ev, "record正常服务中。")