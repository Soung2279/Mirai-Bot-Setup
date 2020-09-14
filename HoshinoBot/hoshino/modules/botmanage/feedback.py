import hoshino
from hoshino import Service, priv
from hoshino.typing import CQEvent
from hoshino.util import DailyNumberLimiter

sv = Service('_feedback_', manage_priv=priv.SUPERUSER, visible=False)

_max = 2
lmt = DailyNumberLimiter(_max)
EXCEED_NOTICE = f'您今天已经喝过{_max}杯了，请明早5点后再来！'

@sv.on_prefix(('来杯咖啡', '反馈信息', '上报信息'))
async def feedback(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(EXCEED_NOTICE, at_sender=True)
    coffee = hoshino.config.SUPERUSERS[0]
    text = str(ev.message).strip()
    if not text:
        await bot.send(ev, "请发送来杯咖啡+您要反馈的内容~", at_sender=True)
    else:
        await bot.send_private_msg(self_id=ev.self_id, user_id=coffee, message=f'QQ为：{uid}的用户在群聊：{ev.group_id}里反馈如下信息：\n{text}')
        await bot.send(ev, f'您的反馈已发送至维护组！如需提交更多信息也可进群：1121815503\n======\n{text}', at_sender=True)
        lmt.increase(uid)
