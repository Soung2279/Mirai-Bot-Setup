import re
import asyncio
from requests import *
from bs4 import *
from nonebot import on_natural_language, NLPSession, IntentCommand, NLPResult
from nonebot import on_command, CommandSession
from .steam import get_steam
import lxml
from hoshino import Service

sv = Service('steam') 

def get_resource():
    url = 'https://www.newyx.net/news/steam1/'
    data = get(url).text
    bs = BeautifulSoup(data, 'lxml').find_all('li', class_='humor')
    return bs


@sv.on_command('喜加一', aliases=('免费领取'))
async def scence(session: CommandSession):
    try:
        a = session.event['group_id']
        if a == 1128254625:
            return
    except:
        pass
    bs = get_resource()
    src = ''
    for i in bs:
        c = i.a.img.get('alt')
        c = str(c).replace("免费领取", "").replace("steam喜加一", '')
        b = i.a.get('href')
        uri = get_steam_url(b)
        if uri is None:
            continue
        src += c + '\n' + str(uri) + '-----------------------\n'
    await session.send(src)


def get_steam_url(url):
    date = get(url).text
    bs = BeautifulSoup(date, 'lxml').find_all('p', style='text-indent:2em;')
    uri = ''
    for i in bs:
        a = i.strong
        if a is None:
            continue
        if re.search('领取地址', i.get_text()) and re.search('\s', i.get_text()):
            uri += i.get_text()
            return uri

@sv.on_command('steam打折', aliases=('steam促销'))
async def scence(session: CommandSession):
    a = ''
    try:
        a = session.event['group_id']
    except:
        pass
    if a == 1128254625:
        return
    bs = get_steam()
    await session.send(bs)