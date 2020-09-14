from nonebot import on_command, CommandSession
import thulac
import hoshino
from hoshino import Service
from .weather import get_weather_of_city
from hoshino import log

sv = Service('weather')

logger = log.new_logger('weather')

@sv.on_command('weather', aliases=('查天气', '查天氣'), only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    weather_report = await get_weather_of_city(city)
    if weather_report:
        await session.send(weather_report)
    else:
        logger.error("Not found weatherInfo")
        await session.send("[ERROR]Not found weatherInfo")


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg
