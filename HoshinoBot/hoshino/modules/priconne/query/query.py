import itertools
from hoshino import util, R
from hoshino.typing import CQEvent
from . import sv

rankjpq = R.img('priconne/quick/日rank前.jpg').cqcode
rankjpz = R.img('priconne/quick/日rank中.jpg').cqcode
rankjph = R.img('priconne/quick/日rank后.jpg').cqcode
ranktwq = R.img('priconne/quick/台rank前.png').cqcode
ranktwz = R.img('priconne/quick/台rank中.png').cqcode
ranktwh = R.img('priconne/quick/台rank后.png').cqcode
rankbq = R.img('priconne/quick/国rank前.png').cqcode
rankbz = R.img('priconne/quick/国rank中.png').cqcode
rankbh = R.img('priconne/quick/国rank后.png').cqcode

@sv.on_fullmatch(('rank表', 'Rank表', 'RANK表'))
async def rank_allask(bot, ev):
    await bot.send(ev, f'请问您要查询哪个服务器的rank表？\n*日rank表\n*台rank表\n*国服rank表')
    return

@sv.on_fullmatch(('日rank表', '日服rank表'))
async def rank_jpask(bot, ev):
    await bot.send(ev, f'请问您要查询哪个位置的rank表？\n**日服前卫rank表\n**日服中卫rank表\n**日服后卫rank表')
@sv.on_fullmatch(('日服前卫rank表', '日服前rank表', '日前rank表'))
async def rank_jpqsend(bot, ev):
    await bot.send(ev, f"日服前卫rank表：{rankjpq}")
@sv.on_fullmatch(('日服中卫rank表', '日服中rank表', '日中rank表'))
async def rank_jpzsend(bot, ev):
    await bot.send(ev, f"日服中卫rank表：{rankjpz}")
@sv.on_fullmatch(('日服后卫rank表', '日服后rank表', '日后rank表'))
async def rank_jphsend(bot, ev):
    await bot.send(ev, f"日服后卫rank表：{rankjph}")
@sv.on_fullmatch(('台rank表', '台服rank表'))
async def rank_twask(bot, ev):
    await bot.send(ev, f'请问您要查询哪个位置的rank表？\n**台服前卫rank表\n**台服中卫rank表\n**台服后卫rank表')
@sv.on_fullmatch(('台服前卫rank表', '台服前rank表', '台前rank表'))
async def rank_twqsend(bot, ev):
    await bot.send(ev, f"台服前卫rank表：{ranktwq}")
@sv.on_fullmatch(('台服中卫rank表', '台服中rank表', '台中rank表'))
async def rank_twzsend(bot, ev):
    await bot.send(ev, f"台服中卫rank表：{ranktwz}")
@sv.on_fullmatch(('台服后卫rank表', '台服后rank表', '台后rank表'))
async def rank_twhsend(bot, ev):
    await bot.send(ev, f"台服后卫rank表：{ranktwh}")
@sv.on_fullmatch(('国服rank表', 'B服rank表', 'b服rank表'))
async def rank_bask(bot, ev):
    await bot.send(ev, f'请问您要查询哪个位置的rank表？\n**国服前卫rank表\n**国服中卫rank表\n**国服后卫rank表')
@sv.on_fullmatch(('国服前卫rank表', '国服前rank表', '国前rank表'))
async def rank_twqsend(bot, ev):
    await bot.send(ev, f"国服前卫rank表：{rankbq}")
@sv.on_fullmatch(('国服中卫rank表', '国服中rank表', '国中rank表'))
async def rank_twzsend(bot, ev):
    await bot.send(ev, f"国服中卫rank表：{rankbz}")
@sv.on_fullmatch(('国服后卫rank表', '国服后rank表', '国后rank表'))
async def rank_twhsend(bot, ev):
    await bot.send(ev, f"国服后卫rank表：{rankbh}")


OTHER_KEYWORDS = '【日rank】【台rank】【b服rank】【黄骑充电表】【一个顶俩】【其它资料】'
PCR_SITES = f'''
【简中wiki/哔哩哔哩公主连结Rwiki】wiki.biligame.com/pcr
【繁中wiki/兰德索尔图书馆】pcredivewiki.tw
【日文wiki/GameWith】gamewith.jp/pricone-re
【日文wiki/AppMedia】appmedia.jp/priconne-redive
【竞技场作业库(中文)】pcrdfans.com/battle
【竞技场作业库(日文)】nomae.net/arenadb
【国服官网】game.bilibili.com/pcr
【日服官网】priconne-redive.jp
【台服官网】www.princessconnect.so-net.tw
【​干炸里脊资源站】​redive.estertion.win

===其他查询关键词===
{OTHER_KEYWORDS}
※B服速查请输入【bcr速查】'''

BCR_SITES = f'''
【卡池亿里眼】bbs.nga.cn/read.php?tid=20816796
【PJJC防守阵容搭配思路】bbs.nga.cn/read.php?tid=22372410
【公会战排名网页端查询】kengxxiao.github.io/Kyouka/
【2020/6月Rank9-3推荐表】bbs.nga.cn/read.php?tid=22247310
【赫斯海德计轴器演示】www.bilibili.com/video/BV16C4y1a7oh?p=1
【角色动作帧数表】bbs.nga.cn/read.php?tid=21952354&_fp=2
【黄骑充电详解】bbs.nga.cn/read.php?tid=21913703&_fp=2
【仓鼠玩家pjjc登顶教程】bbs.nga.cn/read.php?tid=21850496&_fp=2

===其他查询关键词===
{OTHER_KEYWORDS}
※日台服速查请输入【pcr速查】'''

@sv.on_fullmatch(('pcr速查', 'pcr图书馆', '图书馆'))
async def pcr_sites(bot, ev: CQEvent):
    await bot.send(ev, PCR_SITES)
@sv.on_fullmatch(('bcr速查', 'bcr攻略'))
async def bcr_sites(bot, ev: CQEvent):
    await bot.send(ev, BCR_SITES)


YUKARI_SHEET_ALIAS = map(lambda x: ''.join(x), itertools.product(('黄骑', '酒鬼'), ('充电', '充电表', '充能', '充能表')))
YUKARI_SHEET = f'''
{R.img('priconne/quick/黄骑充电.jpg').cqcode}
※大圈是1动充电对象 PvP测试
※黄骑四号位例外较多
※对面羊驼或中后卫坦 有可能歪
※我方羊驼算一号位
※图片搬运自漪夢奈特'''
@sv.on_fullmatch(YUKARI_SHEET_ALIAS)
async def yukari_sheet(bot, ev):
    await bot.send(ev, YUKARI_SHEET)


DRAGON_TOOL = f'''
拼音对照表：{R.img('priconne/KyaruMiniGame/注音文字.jpg').cqcode}{R.img('priconne/KyaruMiniGame/接龙.jpg').cqcode}
龍的探索者們小遊戲單字表 https://hanshino.nctu.me/online/KyaruMiniGame
镜像 https://hoshino.monster/KyaruMiniGame
网站内有全词条和搜索，或需科学上网'''
@sv.on_fullmatch(('一个顶俩', '拼音接龙', '韵母接龙'))
async def dragon(bot, ev):
    await bot.send(ev, DRAGON_TOOL)

OTHER_WEBSITE = f'''
【公会战排名信息网】https://kengxxiao.github.io/Kyouka
【​声优梗和甜心刀阵容】​https://ngabbs.com/read.php?tid=21784456
【论坛/NGA社区】bbs.nga.cn/thread.php?fid=-10308342
【iOS实用工具/初音笔记】bbs.nga.cn/read.php?tid=14878762
【安卓实用工具/静流笔记】bbs.nga.cn/read.php?tid=20499613
​【国服wiki微信小程序】bbs.nga.cn/read.php?tid=21726747
【​公会招募公开版】https://bbs.h-loli.cc/
【​真步真步视界术资料站】https://mahomaho-insight.info/
【小黑盒公主连结wiki】https://api.xiaoheihe.cn/wiki/get_homepage_info_for_app/?wiki_id=1000000040&version=null&is_share=1
​'''
@sv.on_fullmatch(('其他资料', '其他攻略', '更多资料', '更多攻略', '其它资料', '其它攻略'))
async def otherwebsite(bot, ev):
    await bot.send(ev, OTHER_WEBSITE)