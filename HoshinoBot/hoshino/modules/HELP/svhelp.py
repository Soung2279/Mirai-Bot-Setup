from hoshino import R, Service, priv
from hoshino.typing import CQEvent

sv = Service('MANUAL-HELP', manage_priv=priv.SUPERUSER, visible=False, enable_on_default=True)

AICHAT_HELP = '''
基于腾讯AI闲聊的群聊功能。
由于代码层原因，目前仅支持群聊被动触发(即bot会自己在群内回复。)
在大多数情况下，都只建议您使用[关闭对线]来降低bot发言频率（2020-9-4，bug尚未修复，此指令无效）
会战期间bot主人将停用此项功能，以免出现不必要的误解
=========
*指令需独立完整匹配*
=========
[开启对线]  #设置bot为100%几率被动发言，即理论上群聊里每一条消息都将回复（请注意：因为群聊消息较多，若bot未匹配到相应的回答，将不会回复）
[关闭对线]  #设置bot为10%几率被动发言
[禁用 aichat]  #停用bot对话闲聊功能
'''.strip()
@sv.on_fullmatch(('aichat帮助', 'aichat说明'))
async def aichat_help(bot, ev: CQEvent):
        await bot.send(ev, f"{AICHAT_HELP}")

AIRCON_HELP = '''
娱乐向功能：模拟空调运行。
这个服务将群视为一个房间，每位群员对应2m³的空气，不足20m³的以20m³算。
家用空调的基准风量为0.178m³/s，基准功率为5000W，中档和高档为基准的1.2与1.5倍，基准数据来源于一款常见家用空调的官方网站
中央空调将群划分为100m³的房间，不足一间的以一间计，每间房间配备一台功率7500W，循环风量0.577m³的空调，数据来源于一家著名空调制造商的官方网站。
=========
*指令需独立完整匹配*
*注意空格*
=========
[开空调/关空调]  #开/关空调
[当前温度]  #查看当前温度
[设置温度/设置环境温度 <温度>]  #设置温度或环境温度
[设置风速 <档位>]  #设置风速
[空调类型]  #查看空调类型
[升级空调/降级空调]  #调整空调类型
'''.strip()
@sv.on_fullmatch(('aircon帮助', 'aircon说明'))
async def aircon_help(bot, ev: CQEvent):
        await bot.send(ev, f"{AIRCON_HELP}")

FEEDBACK_HELP = '''
简易反馈功能。通过bot将信息上报到bot维护组。
每人日上限2次。您也可以加入群：1121815503联系
=========
*指令需独立完整匹配*
*注意空格*
=========
[来杯咖啡] +需要上报的信息  #上报信息给bot维护组
'''.strip()
@sv.on_fullmatch(('feedback帮助', 'feedback说明'))
async def feedback_help(bot, ev: CQEvent):
        await bot.send(ev, f"{FEEDBACK_HELP}")
        #await bot.send(ev, f"使用例：{R.img('emample/feedback演示.jpg').cqcode}")

CALENDAR_HELP = '''
公主连结日程表查阅推送。
可自定义日程地区和推送时间
=========
*指令需独立完整匹配*
=========
[日历|本周日历|今日日历|明日日历]  #查看日程表
[切换日程]  #切换日程表地区
[设置日程时间]  #切换日程表每日推送时间
[查看日程地区]  #查看本群日程表地区
[查看日程时间]  #查看本群日程表推送时间
[停止推送日程]  #停止推送日程
[开始推送日程]  #开始推送日程
'''.strip()
@sv.on_fullmatch(('calendar帮助', 'calendar说明'))
async def calendar_help(bot, ev: CQEvent):
        await bot.send(ev, f"{CALENDAR_HELP}")

DICE_HELP = '''
简易模拟掷骰子。也可用作取随机数用。
不指定骰子面数默认为100面。
=========
*指令需独立完整匹配*
*注意小写与空格*
=========
[.r]  #模拟掷100面骰子1次
[.r xdy]  #掷x次y面骰子
'''.strip()
@sv.on_fullmatch(('dice帮助', 'dice说明'))
async def dice_help(bot, ev: CQEvent):
        await bot.send(ev, f"{DICE_HELP}")

FLAC_HELP = '''
无损音乐资源搜索。数据来源：www.acgjc.com
bot不保证资源的可用性
=========
*指令需独立完整匹配*
=========
[搜无损] +歌名  #关键词搜索歌曲资源
'''.strip()
@sv.on_fullmatch(('flac帮助', 'flac说明'))
async def flac_help(bot, ev: CQEvent):
        await bot.send(ev, f"{FLAC_HELP}")

GENERATOR_HELP = '''
文章/表情包 生成器
文章可选营销号，狗屁不通，舔狗日记（这个要自己写！）
表情包可选记仇，无中生友，pcr表情包
=========
*需完整独立匹配指令*
*注意有斜线和空格*
=========
[营销号 主体/事件/另一种说法]  #营销号生成器
[狗屁不通 主题]  #狗屁不通生成器
[记仇 天气/主题]  #记仇表情包生成器
[我朋友说他好了]  #无中生友，无艾特时随机群员
[日记 天气/主题]  #舔狗日记生成器（需要自己写！）
[表情列表]  #查看bot的表情库存
[更新表情]  #刷新一下bot的表情库存
[查看表情 <名字>]  #查看指定表情
[生成表情 <名字> <文案>]  #生成一张表情
[上传表情 <名字> <图片>]  #自己上传一张表情，需要使用者是管理员
[删除表情 <名字>]  #删除一张表情，需要使用者是管理员
'''.strip()
@sv.on_fullmatch(('generator帮助', 'generator说明', 'generator-text帮助' ,'generator-text说明' ,'generator-image帮助' ,'generator-image说明'))
async def generator_help(bot, ev: CQEvent):
        await bot.send(ev, f"{GENERATOR_HELP}")

REPEATER_HELP = '''
随机复读功能。用以辅助群内闲聊
从第2条复读，即第3条重复消息开始有几率触发复读
复读率随复读次数逐渐增加。
=========
*此功能无需指令*
=========
[禁用 repeater]  #关闭随机复读功能
'''.strip()
@sv.on_fullmatch(('repeater帮助', 'repeater说明'))
async def repeater_help(bot, ev: CQEvent):
        await bot.send(ev, f"{REPEATER_HELP}")

BOTCHAT_HELP = '''
轻量语言库。用以辅助群内闲聊
通过群聊内的关键词几率触发回复（例如对部分梗bot会有回复）
bot的人物设定基于此功能体现
bot的自检和运行信息也基于此回复
=========
*此功能无需指令*
=========
[@bot自检]  #检查早坂爱bot运行状况，如有回复则运行正常
[框架信息]  #开发人员用-用于确认bot目前的框架版本
[禁用 botchat]  #关闭轻量语言库
'''.strip()
@sv.on_fullmatch(('botchat帮助', 'botchat说明'))
async def botchat_help(bot, ev: CQEvent):
        await bot.send(ev, f"{BOTCHAT_HELP}")

PCRWARN_HELP = '''
定时提醒功能。区分服务器（国台/日）
目前设定的提醒时段有：
商店刷新，日常体力刷新，每日任务刷新，竞技场结算提醒
=========
*此功能无需指令*
=========
[禁用 pcrwarn_land/jp]  #关闭定时提醒功能
'''.strip()
@sv.on_fullmatch(('pcrwarn帮助', 'pcrwarn说明', 'pcrwarn-land帮助', 'pcrwarn-land说明', 'pcrwarn-jp帮助', 'pcrwarn-jp说明'))
async def pcrwarn_help(bot, ev: CQEvent):
        await bot.send(ev, f"{PCRWARN_HELP}")

BLACKLIST_HELP = '''
公会人员公开黑名单功能。数据来源：docs.qq.com/sheet/DV1JqSHJ5aEVNUG1q
名单来源：nga风纪区（现为兰德索尔广场）
名单可信度请自行判断。若有误判或漏判本bot概不负责
数据于每日8点更新
=========
*需完整独立匹配指令*
*注意没有空格*
=========
[失信1919810]  #根据游戏UID搜索
[失信114514]  #根据QQ搜索
'''.strip()
@sv.on_fullmatch(('blacklist帮助', 'blacklist说明'))
async def blacklist_help(bot, ev: CQEvent):
        await bot.send(ev, f"{BLACKLIST_HELP}")

CLANRANK_HELP = '''
实时查询公会排名功能。数据来源：kengxxiao.github.io/Kyouka
数据刷新时间为30分钟一次,相比于游戏内排名有约30分钟延迟
无法查询25001之后的公会与新建公会，有多条记录时仅显示前10条信息
=========
*需完整独立匹配指令*
=========
[绑定公会] +会长UID  #为一个公会绑定信息, 需要会长ID，绑定之后可直接群里查询不用跟名字
[查询会长 卢本伟]  #查询会长名字包含卢本伟的公会排名
[查询公会 卢本伟]  #查询公会名字包含卢本伟的公会排名
[查询排名 5000]  #查看5000名的公会分数信息
[分数线]  #通过line接口来查询分数线，共14条信息
'''.strip()
@sv.on_fullmatch(('clanrank帮助', 'clanrank说明'))
async def clanrank_help(bot, ev: CQEvent):
        await bot.send(ev, f"{CLANRANK_HELP}")

EXPLOSION_HELP = '''
和惠惠每天练习一发爆裂魔法！
每人每天上限一发，可以重置
=========
*需完整独立匹配指令*
=========
[爆裂魔法]  #随机练习一发爆裂魔法
[@bot补魔]  #恢复魔力
'''.strip()
@sv.on_fullmatch(('explosion帮助', 'explosion说明'))
async def arena_help(bot, ev: CQEvent):
        await bot.send(ev, f"{EXPLOSION_HELP}")

ARENA_HELP = '''
竞技场作业查询功能。数据来源：pcrdfans.com
因作业网负载较大，高峰期可能无法查询，请见谅。
=========
*注意空格*
=========
[怎么拆] +防守队角色名  #查询竞技场解法
[点赞] +作业id  #评价作业
[点踩] +作业id  #评价作业
'''.strip()
@sv.on_fullmatch(('arena帮助', 'arena说明'))
async def arena_help(bot, ev: CQEvent):
        await bot.send(ev, f"{ARENA_HELP}")

GACHA_HELP = '''
模拟抽卡功能。使用本地卡池数据。
卡池数据可能不会及时更新，请见谅
=========
*指令已做语言兼容化，近似关键词均可触发*
*需@bot或呼唤bot呢称*
=========
[来发十连]  #模拟十连抽奖
[来发单抽] #模拟单抽
[来一井]  #模拟4w5一井
（无需@）[查看卡池]  #查看当前模拟卡池信息
（无需@）[切换卡池]  #更换模拟卡池
（无需@）[氪金@xxx]  #群管理使用此指令来重置抽卡次数限制，可@多人
'''.strip()
@sv.on_fullmatch(('gacha帮助', 'gacha说明'))
async def gacha_help(bot, ev: CQEvent):
        await bot.send(ev, f"{GACHA_HELP}")

NEWS_HELP = '''
公主连结R官方新闻推送功能。区分台服和国服
日服由于网络环境原因暂不支持
=========
*没有指令*
=========
[启用 news-bili]  #开启国服新闻推送
'''.strip()
@sv.on_fullmatch(('news帮助', 'news说明', 'news-bili帮助', 'news-bili说明', 'news-tw帮助', 'news-tw说明'))
async def news_help(bot, ev: CQEvent):
        await bot.send(ev, f"{NEWS_HELP}")

CHERUGO_HELP = '''
切噜语（ちぇる語, Language Cheru）转换
=========
*指令需完整独立匹配*
*注意有♪符号哦*
=========
[切噜一下] +内容  #将文字转换为切噜语
[切噜～♪] +切噜语  #切噜语翻译
'''.strip()
@sv.on_fullmatch(('cherugo帮助', 'cherugo说明', 'pcr-cherugo帮助', 'pcr-cherugo说明'))
async def cherugo_help(bot, ev: CQEvent):
        await bot.send(ev, f"{CHERUGO_HELP}")

QUERY_HELP = '''
PCR实用查询功能。数据来源：nga，哔哩哔哩，youtube等
使用本地数据，所以可能不是最新攻略，请见谅。
此服务控制三个小功能：
rank表、简易攻略速查、充电表等
jjc挖矿余量查询
简易角色查询
=========
*指令需完整独立匹配*
=========
[rank表]  #查看rank推荐表
[pcr速查]  #查询pcr通用资料
[bcr速查]  #查询适合国服的攻略
[黄骑充电表]  #查询黄骑充电原理表
[拼音接龙]  #查询注音文字对照表
[其他资料]  #查询其他资料
[挖矿15001]  #矿场余钻查询
[谁是优衣]  #角色别称查询
'''.strip()
@sv.on_fullmatch(('query帮助', 'query说明', 'pcr-query帮助', 'pcr-query说明'))
async def query_help(bot, ev: CQEvent):
        await bot.send(ev, f"{QUERY_HELP}")

COMIC_HELP = '''
官方四格漫画推送(日文)与查阅
=========
*指令已做语言兼容化，近似关键词均可触发*
*注意空格*
=========
[官漫] +编号  #阅览指定话漫画
'''.strip()
@sv.on_fullmatch(('comic帮助', 'comic说明'))
async def comic_help(bot, ev: CQEvent):
        await bot.send(ev, f"{COMIC_HELP}")

QA_HELP = '''
你问我答功能。用以辅助群内闲聊
输入问题和回答记录到bot里
=========
*指令没有空格！请注意*
=========
[我问xxx你答yyy]  #记录个人Q&A
[有人问xxx你答yyy]  #记录群聊Q&A，需要群管理权限
[不要回答]+问题  #删除问答
[查看QA]  #查看当前群记录的问答
'''.strip()
@sv.on_fullmatch(('qa帮助', 'qa说明', 'QA说明' ,'QA帮助'))
async def qa_help(bot, ev: CQEvent):
        await bot.send(ev, f"{QA_HELP}")

SETU_HELP = '''
随机涩图服务。源：本地图库(目前存余700+)
默认每人日上限20次，间隔冷却时间3s，重置次数无限制
选取图为广义上的非r18涩图，且依据我的喜好选择，鲜有漏点图。
因为mirai框架限制和tx方原因，屡有无法正常发图的情况，请见谅。
=========
*指令做了部分语言兼容化，例如涩图=色图=瑟图*
*使用本功能即视为您知晓其风险*
*请勿滥用*
=========
[不够涩][再来点][看过了][铜/铯][来一份瑟图][我要看色图][来点涩图]
[换肾/补肾/换弹夹/换蛋夹]@xxx  # 群管理使用此指令来重置日调用限制，可@多人
'''.strip()
@sv.on_fullmatch(('setu帮助', 'setu说明'))
async def setu_help(bot, ev: CQEvent):
        await bot.send(ev, f"{SETU_HELP}")

WCLOUD_HELP = '''
短篇网抑云语录。源：api.heerdev.top/nemusic/random
=========
*指令需完整独立匹配*
=========
[生而为人][网抑云][到点了]  #随机一篇网抑云语录
'''.strip()
@sv.on_fullmatch(('wcloud帮助', 'wcloud说明'))
async def wcloud_help(bot, ev: CQEvent):
        await bot.send(ev, f"{WCLOUD_HELP}")

RDIMG_HELP = '''
指定关键词发出图片。源：本地图库
因为建立的图库较少，内容较贫乏，不建议使用。
=========
*指令需完整独立匹配*
=========
[来点pcr表情包] #发送pcr公会表情包
[来点猫猫头]  #发送猫猫头表情包
[来点可可萝]  #随机发送可可萝的图
'''.strip()
@sv.on_fullmatch(('rdimg帮助', 'rdimg说明'))
async def rdmig_help(bot, ev: CQEvent):
        await bot.send(ev, f"{RDIMG_HELP}")

HOURCALL_HELP = '''
整点时报功能。从本地的若干组时报文本中随机调取
建议不要在活跃度较低的群内启用
=========
*指令需完整独立匹配*
=========
[禁用hourcall] #停用时报功能
'''.strip()
@sv.on_fullmatch(('hourcall帮助', 'hourcall说明'))
async def hourcall_help(bot, ev: CQEvent):
        await bot.send(ev, f"{HOURCALL_HELP}")

VORTUNE_HELP = '''
Visual YouTuber运势签。若干组vtb模板中随机抽签。
其中“白上吹雪”可指定（不要问我为什么只有fbk）
=========
*指令需完整独立匹配*
=========
[抽签] #来一签
[小狐狸签]  #来一签fbk定制签
'''.strip()
@sv.on_fullmatch(('vortune帮助', 'vortune说明'))
async def vtb_help(bot, ev: CQEvent):
        await bot.send(ev, f"{VORTUNE_HELP}")

RUSSIAN_HELP = '''
模拟俄罗斯转盘。
=========
*指令需完整独立匹配*
=========
[俄罗斯转盘] #开始游戏，装填子弹
[开枪]  #开始游戏
'''.strip()
@sv.on_fullmatch(('russian帮助', 'russian说明'))
async def russian_help(bot, ev: CQEvent):
        await bot.send(ev, f"{RUSSIAN_HELP}")

SEARCH_HELP = '''
识别图片来源。源：SauceNao.com
番剧出处查询，识别国漫效果较差
=========
*指令做了部分语言兼容化*
=========
[识图+图片]  #查询图片来源
[搜番+图片]  #根据图片查询番剧
'''.strip()
@sv.on_fullmatch(('search帮助', 'search说明', 'search-image帮助', 'search-image说明', 'search-anime帮助', 'search-anime说明'))
async def picfinder_help(bot, ev: CQEvent):
        await bot.send(ev, f"{SEARCH_HELP}")

HORSE_HELP = '''
简易模拟赛🐎，会有短暂刷屏
=========
*指令需完整独立匹配*
=========
[赛马开始]  #开始模拟赛跑
[选中] +角色名  #选择比赛角色
'''.strip()
@sv.on_fullmatch(('horse帮助', 'horse说明', 'pcr-horse帮助', 'pcr-horse说明'))
async def horse_help(bot, ev: CQEvent):
        await bot.send(ev, f"{HORSE_HELP}")

BUP_HELP = '''
B站up动态。基于RSS订阅
目前已经订阅官方：pcr/明日方舟
非官方：山新，hanser，泠鸢
vtb：白上吹雪，赤井心，夏色祭，神楽七奈，阿库娅，鹿乃，兔田佩克拉，神乐mea，爱酱，本间向日葵
（不要问为啥只有这些）
因为过多订阅可能造成打扰，建议酌情启用
=========
*指令需完整独立匹配*
=========
[禁用 pcr国服推送]
[禁用 明日方舟推送]
[禁用 B站up动态]
[禁用 vtb推送]
'''.strip()
@sv.on_fullmatch(('推送帮助', '推送说明'))
async def bup_help(bot, ev: CQEvent):
        await bot.send(ev, f"{BUP_HELP}")

LIVENT_HELP = '''
直播提醒。可自己添加订阅，目前仅支持斗鱼和bilibili
=========
*指令需完整独立匹配*
=========
[live]  #根据提示订阅一个直播间
'''.strip()
@sv.on_fullmatch(('直播推送帮助', '直播推送说明'))
async def livent_help(bot, ev: CQEvent):
        await bot.send(ev, f"{LIVENT_HELP}")

BVOTE_HELP = '''
B站up投稿提醒。可自己添加订阅
=========
*指令需完整独立匹配*
=========
[video]  #根据提示订阅B站up的投稿提醒
'''.strip()
@sv.on_fullmatch(('B站投稿提醒帮助', 'B站投稿提醒说明'))
async def bvote_help(bot, ev: CQEvent):
        await bot.send(ev, f"{BVOTE_HELP}")

REPORT_HELP = '''
公会战报告图生成。注意，hoshino版和yobot版不互通，且使用方式有略微出入。
请向群管理或bot维护组确认本群使用何种会战管理功能
=========
*指令需完整独立匹配*
*符号已做全半角兼容，！或!均能触发指令*
=========
&- hoshino -&
[!离职报告]  #生成一张本期离职报告
[!会战报告]  #生成一张本期会战报告
[!看看报告 @qq]  #管理员查看群友的会战报告。若at了多人，会显示最后一人的报告。
[!出刀时间统计]  #生成一张本公会此次公会战的出刀时间分布统计

&- yobot -&
[生成会战报告] @用户 +API地址  #生成会战报告，如果设置了本群api则无需附带API地址，如果仅输出本人的报告直接输入指令即可
[生成离职报告] @用户 +API地址  #生成离职报告，操作同上
[设置工会api] +API地址  #(需要管理员权限)为本群设置默认的Yobot工会API，此API可在网页的[统计]页面获取
[查看工会api]  #(需要管理员权限)查看本群设置的Yobot API
[清除工会api]  #(需要管理员权限)清除本群设置的Yobot API
'''.strip()
@sv.on_fullmatch(('report帮助', 'report说明', 'report-yobot帮助', 'report-yobot说明', 'report-hoshino帮助', 'report-hoshino说明'))
async def report_help(bot, ev: CQEvent):
        await bot.send(ev, f"{REPORT_HELP}")

GUESS_HELP = '''
猜角色小游戏！好玩且有难度！
目前只能猜pcr的角色
回答只能是中文原名！（可以搭配另一项功能通过别称查原名）
=========
*指令需完整独立匹配*
=========
[猜头像]  #猜猜机器人随机发送的头像的一小部分来自哪位角色
[猜头像群排行]  #显示猜头像小游戏猜对次数的群排行榜(只显示前十名)
[猜角色]  #猜猜机器人随机发送的文本在描述哪位角色
[猜角色群排行]  #显示猜角色小游戏猜对次数的群排行榜(只显示前十名)
'''.strip()
@sv.on_fullmatch(('guess帮助', 'guess说明', 'guess-icon帮助', 'guess-icon说明', 'guess-text帮助', 'guess-text说明'))
async def guess_help(bot, ev: CQEvent):
        await bot.send(ev, f"{GUESS_HELP}")

SHOUQUAN_HELP = '''
查群内授权情况，因为篇幅较长所以整合了一下
=========
*指令需完整独立匹配*
=========
[充值帮助]  #呼出帮助文档
'''.strip()
@sv.on_fullmatch(('授权帮助', '授权说明', '群授权帮助', '群授权说明', '机器人授权帮助', '机器人授权说明'))
async def authms_help(bot, ev: CQEvent):
        await bot.send(ev, f"{SHOUQUAN_HELP}")
        
LAOPO_HELP = '''
群老婆(阴间功能)
=========
*指令需完整独立匹配*
=========
[老婆]  #生成老婆或呼唤老婆
[老婆的个人信息]  #查看当前老婆的信息
[老婆骂我]  #随机发言
[结婚]  #结婚
[老婆！/爱我/爱你]  #随机发言
[分手]  #和老婆分手
[我的渣男值]  #分手看的
'''.strip()
@sv.on_fullmatch(('laopo帮助', 'laopo说明', '老婆帮助', '老婆说明'))
async def laopo_help(bot, ev: CQEvent):
    await bot.send(ev, f"LAOPO_HELP")
    
PIXIV_HELP = '''
p站搜图功能
=========
*指令需完整匹配*
=========
[来一份XX色图]  #搜索XX的色图
'''.strip()
@sv.on_fullmatch(('pixiv帮助', 'pixiv说明'))
async def pixiv_help(bot, ev: CQEvent):
    await bot.send(ev, f"PIXIV_HELP")