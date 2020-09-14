from requests import *
from bs4 import *
import lxml
import asyncio
import nest_asyncio
nest_asyncio.apply()


tasks = []
index = []


def get_resource():
    url = 'https://store.steampowered.com/specials#tab=TopSellers'
    data = get(url).text
    bs = BeautifulSoup(data, 'lxml').find_all('div', id='TopSellersRows')
    temp = BeautifulSoup(str(bs), 'lxml').find_all('a')
    return temp


async def star(bs):
    temp = BeautifulSoup(str(bs), 'lxml')
    b = bs.get('href')
    name = temp.find_all('div', class_='tab_item_name')[0].get_text()
    zheKou = '打折：' + temp.find_all('div', class_='discount_pct')[0].get_text() + '\n'
    Resource_piece = '原价:' + temp.find_all('div', class_='discount_original_price')[0].get_text() + '\n'
    now_piece = '现价：' + temp.find_all('div', class_='discount_final_price')[0].get_text() + '\n'
    test = name + '\n' + zheKou + Resource_piece + now_piece + str(b) + '\n------------------------------------\n'
    index.append(test)


def run():
    loop = asyncio.get_event_loop()
    for i in tasks:
        loop.run_until_complete(i)
        tasks.remove(i)


def get_steam():
    bs = get_resource()
    for i in bs:
        task = asyncio.ensure_future(star(i))
        tasks.append(task)
    run()
    src=''
    for j in index:
        src+=j
    return src
