from nonebot import *
import json
from random import randint
import asyncio

import os

bot = get_bot()
fd = os.path.dirname(__file__)

with open(os.path.join(fd , 'rsdata.json')) as f:
    data = json.load(f)
with open(os.path.join(fd , 'rsplayer.json')) as f:
    player = json.load(f)


def save(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)


# main part
@on_command('rs', aliases=('俄罗斯轮盘','开枪'), only_to_me=False)
async def spin(session: CommandSession):
    if session.ctx['message_type'] == 'private':
        msg = '此功能仅适用于群聊'
        session.finish(msg)

    else:
        user = str(session.ctx['user_id'])
        group = session.ctx['group_id']
        if group not in player:
            player[group] = {}
        if user not in player[group]:
            player[group][user] = {}
            if session.ctx.sender['card'] is not None:
                player[group][user]['nickname'] = session.ctx.sender['card']
            else:
                player[group][user]['nickname'] = session.ctx.sender['nickname']
            player[group][user]['win'] = 0
            player[group][user]['death'] = 0
            
        if group not in data:
            data[group] = {}
            data[group]['curnum'] = 0
            data[group]['next'] = 1
            
            

        if data[group]['curnum'] <= 0:
            msg = '欢迎参与紧张刺激的俄罗斯轮盘活动，请输入要填入的子弹数目(最多6颗)'
            bullet = int(session.get('bullet', prompt=msg))
            if bullet == 6:
                ans = session.get('ans', prompt="你认真的？(y/n)")
                if ans == 'y':
                    data[group]['curnum'] = bullet
                    data[group]['next'] = 0
                    await session.send("装填完毕")
                else:
                    session.finish("请重新开始")
            elif bullet < 1 or bullet > 6:
                session.finish("数目不正确，请重新开始.")
            else:
                data[group]['curnum'] = bullet
                data[group]['next'] = randint(0, 6 - data[group]['curnum'])
                await session.send("装填完毕")

        else:
            if data[group]['next'] == 0:
                await session.send("很不幸，你死了......")
                # await bot.set_group_ban(group_id=group, user_id=int(user), duration=60)
                player[group][user]['death'] += 1
                data[group]['curnum'] -= 1
                data[group]['next'] = randint(0, 6 - data[group]['curnum'])
                if data[group]['curnum'] <= 0:
                    await session.send("感谢各位的参与，让我们看一下游戏结算:")
                    await asyncio.sleep(1)
                    msg = ''
                    for k, i in player[group].items():
                        msg += ("%s:  胜利: %s   死亡: %s\n" % (i['nickname'], i['win'], i['death']))
                    
                    player[group] = {}
                    
                    data[group]['curnum'] = 0
                    data[group]['next'] = 1
                    
                    player.clear()
                    await session.send(msg)
                else:
                    await session.send("欢迎下一位.还剩%d发" % data[group]['curnum'])
            else:
                data[group]['next'] -= 1
                msg = "你活了下来，下一位.还剩%d发" % data[group]['curnum']
                player[group][user]['win'] += 1
                await session.send(msg)

        save(data, os.path.join(fd , 'rsdata.json'))
        save(player, os.path.join(fd , 'rsplayer.json'))
