import re
import math
import random

from hoshino import Service, util
from hoshino.typing import CQEvent

sv = Service('sleeping-set',visible=False)

@sv.on_fullmatch(('睡眠套餐', '休眠套餐', '精致睡眠', '来一份精致睡眠套餐'))
async def sleep_8h(bot, ev):
    await util.silence(ev, 8*60*60, skip_su=False)


@sv.on_rex(r'(来|來)(.*(份|个)(.*)(睡|茶)(.*))套餐')
async def sleep(bot, ev: CQEvent):
    base = 0 if '午' in ev.plain_text else 5*60*60
    length = len(ev.plain_text)
    sleep_time = base + round(math.sqrt(length) * 60 * 30 + 60 * random.randint(-15, 15))
    await util.silence(ev, sleep_time, skip_su=False)
