from nonebot import on_command, CommandSession
from kth_timeoutdecorator import TimeoutException
import hoshino
from .japanese import get_definition_of_word
from hoshino import log, Service

sv = Service('japanese')

logger = log.new_logger('japanese')

@sv.on_command('jpd', aliases=('日典', 'jd'), only_to_me=False)
async def jpd(session: CommandSession):
    word = session.get('word', prompt='你想查询哪个单词呢？')
    jpd_report = ""
    try:
        jpd_report = await get_definition_of_word(word)
    except TimeoutException as e:
        logger.error("Timeout! {}".format(e))
        jpd_report = "[ERROR]Timeout!"
        
    if jpd_report:
        await session.send(jpd_report)
    else:
        logger.error("Not found jpdInfo")
        await session.send("[ERROR]Not found jpdInfo")


@jpd.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['word'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的单词不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg
