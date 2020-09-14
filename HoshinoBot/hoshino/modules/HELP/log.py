from nonebot import on_command
from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('botlog', manage_priv=priv.SUPERUSER, visible=False, enable_on_default=True)

LOG = '''
2020.9.4 bot更新日志
=====================
修复：
[clanrank]现在可以正常查询会战排名了。
[generator]现在可以正常使用【我朋友说】生成图片了

更新：
[HoshinoBot]服务列表优化，隐藏了不必要的服务并对部分功能近似的服务进行分组命名
[yobot]会战网页美化
[HELP]增添帮助文本
[explosion]爆裂魔法，它回来了！
[wcloud]新的网抑云实现方式，更为生动
[botchat]新鲜的梗补充，原来的语音回来了，并且现在的早安/晚安更加智能

新增：
[authMS]bot全面授权系统，若漏掉本群请及时联系群bot维护
[guess]猜角色小游戏，可以通过头像和文本猜，发送【guess帮助】了解
[translate]机翻译文，群管理可用（比较鸡肋）

遗留：
[aichat]权限bug，目前仍然只有bot主人才可以控制对线模式
[record]新的角色语音试听功能正在迁移（转换文件格式）
[mirai]（可能）有意外的bug出现（mirai-1.0-M3-1）/（cqhttp-0.2.3）

额外：
近期准备添加一个每日罗翔案例的小功能（懒，有时间就写）
最近连着几个bot被冻结了，这段时间还希望各位不要滥用bot
=====================
如有建议请使用【来杯咖啡】或进入群聊：1121815503
- 请珍惜bot尚存群内的时光 -
'''.strip()

@sv.on_fullmatch(('botlog', '更新日志'))
async def update_log(bot, ev):
    await bot.send(ev, f"{LOG}")
