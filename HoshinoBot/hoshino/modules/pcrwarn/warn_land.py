import os
from datetime import datetime

import hoshino
from hoshino import Service, priv, R

svbl = Service('pcrwarn-land', enable_on_default=True, manage_priv=priv.ADMIN, visible=True)

@svbl.scheduled_job('cron', hour='6')
async def day1_reminder():
    path = 'C:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(1/4){R.img("yao.jpg").cqcode}\n', 
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'day1_reminder')

@svbl.scheduled_job('cron', hour='12')
async def day2_reminder():
    path = 'C:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(2/4){R.img("yao.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'day2_reminder')

@svbl.scheduled_job('cron', hour='18')
async def day3_reminder():
    path = 'C:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(3/4){R.img("yao.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{F:/Resources/pcrwarn/要感谢我哦.mp3}]'
    ]
    await svbl.broadcast(msgs, 'day3_reminder')
    
@svbl.scheduled_job('cron', hour='23', minute='59')
async def day4_reminder():
    path = 'C:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(4/4){R.img("yao.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'day4_reminder')  

@svbl.scheduled_job('cron', hour='14', minute='40')
async def beici():
    path = 'C:/Resources/pcrwarn/呐。天气这么好，我们出去玩吧.mp3'
    msgs = [
        f'现在是北京时间14点40，距离竞技场结算还有20分钟哦！请注意！{R.img("randomimg/ma/ma5.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'beici')
    
@svbl.scheduled_job('cron', hour='5')
async def wakeup():
    path = 'C:/Resources/pcrwarn/（小哼）.mp3'
    msgs = [
        f'你醒了么~~我这就为您准备早餐！{R.img("randomimg/ma/ma2.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'wakeup') 

@svbl.scheduled_job('cron', hour='12')
async def tili1():
    path = 'C:/Resources/pcrwarn/呐，便当也给我一点吧.mp3'
    msgs = [
        f'中午的游戏体力可以领取了哦！{R.img("randomimg/ma/ma17.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'tili1')     
    
@svbl.scheduled_job('cron', hour='18')
async def tili2():
    path = 'C:/Resources/pcrwarn/呐，便当也给我一点吧.mp3'
    msgs = [
        f'下午的游戏体力可以领取了哦！{R.img("randomimg/ma/ma1.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'tili2') 
    
@svbl.scheduled_job('cron', hour='0', minute='30')
async def sleep():
    path = 'C:/Resources/pcrwarn/那就这样，贵安.mp3'
    msgs = [
        f'已经12点半了哦~你也要早点休息！{R.img("randomimg/ma/ma13.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svbl.broadcast(msgs, 'sleep') 