import requests,random,os,json,re
from hoshino import Service,R,priv
from hoshino.typing import CQEvent
from hoshino.util import FreqLimiter
import hoshino
sv = Service('wcloud', enable_on_default=True, visible=True, manage_priv=priv.ADMIN)

_time_limit = 3
_lmt = FreqLimiter(_time_limit)

def pic_gender_cqcode(dic_name):
    '''
    获得/res/img/dic_name目录下一张随机图片，返回cqcode
    '''
    pic_dir = R.img(dic_name).path
    
    file_list:list = os.listdir(pic_dir)
    img_random = random.choice(file_list)
    img_path = dic_name + '/' + img_random
    img_cqcode = R.img(str(img_path)).cqcode
    return img_cqcode

def get_nt_words():
    if os.path.exists('./hoshino/modules/wcloud/nt_words.json'):
        with open('./hoshino/modules/wcloud/nt_words.json',"r",encoding='utf-8') as dump_f:
            try:
                # 读取错误一般是人工改动了config并且导致json格式错误
                words = json.load(dump_f)
            except Exception as e:
                hoshino.logger.error(f'读取网抑云语录时发生错误{type(e)}')
                return None
    else:
        hoshino.logger.error(f'目录下未找到网抑云语录')
    keys = list(words.keys())
    key = random.choice(keys)

    return words[key]["text"]


@sv.on_keyword(('生而为人','生不出人','网抑云','已黑化','到点了'))
async def net_ease_cloud_word(bot,ev:CQEvent):
    gid = ev.group_id
    if random.random()<0.90:
        if not _lmt.check(gid):
        # 冲太多...哦不是, 抑郁太多对身体不好
            await bot.send(ev, '抑郁太多对身体不好,请等待一会儿哦', at_sender=True)
            return
        _lmt.start_cd(gid)
        try:
            sentences = pic_gender_cqcode('wcloud/success')
        except Exception as e:
            hoshino.logger.error(f'获取目录res/img/wcloud/success下的图片时发生错误{type(e)}, 请检查')
            sentences = ''
    
        nt_word = get_nt_words()
        sentences += nt_word
        await bot.send(ev, sentences)
    else:
        await bot.send(ev, R.img(f"wcloud/failed/nowc{random.randint(1, 7)}.jpg").cqcode)
        await bot.send(ev, f'上号失败，不准抑郁')
