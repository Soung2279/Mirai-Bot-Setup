import os
from datetime import datetime

from hoshino import Service, priv, R

svjp = Service('pcrwarn-jp', enable_on_default=False, manage_priv=priv.ADMIN, visible=True)

@svjp.scheduled_job('cron', hour='5')
async def day1_reminder():
    path = 'F:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(1/4){R.img("yao.jpg").cqcode}\n', 
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'day1_reminder')

@svjp.scheduled_job('cron', hour='11')
async def day2_reminder():
    path = 'F:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(2/4){R.img("yao.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'day2_reminder')

@svjp.scheduled_job('cron', hour='17')
async def day3_reminder():
    path = 'F:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(3/4){R.img("yao.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{F:/Resources/pcrwarn/要感谢我哦.mp3}]'
    ]
    await svjp.broadcast(msgs, 'day3_reminder')
    
@svjp.scheduled_job('cron', hour='23')
async def day4_reminder():
    path = 'F:/Resources/pcrwarn/要感谢我哦.mp3'
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(4/4){R.img("yao.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'day4_reminder')  

@svjp.scheduled_job('cron', hour='13', minute='40')
async def beici():
    path = 'F:/Resources/pcrwarn/呐。天气这么好，我们出去玩吧.mp3'
    msgs = [
        f'现在是日本时间14点40，距离竞技场结算还有20分钟哦！请注意！{R.img("randomimg/ma/ma5.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'beici')
    
@svjp.scheduled_job('cron', hour='4')
async def wakeup():
    path = 'F:/Resources/pcrwarn/（小哼）.mp3'
    msgs = [
        f'你醒了么~~我这就为您准备早餐！{R.img("randomimg/ma/ma2.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'wakeup') 

@svjp.scheduled_job('cron', hour='11')
async def tili1():
    path = 'F:/Resources/pcrwarn/呐，便当也给我一点吧.mp3'
    msgs = [
        f'中午的游戏体力可以领取了哦！{R.img("randomimg/ma/ma17.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'tili1')     
    
@svjp.scheduled_job('cron', hour='17')
async def tili2():
    path = 'F:/Resources/pcrwarn/呐，便当也给我一点吧.mp3'
    msgs = [
        f'下午的游戏体力可以领取了哦！{R.img("randomimg/ma/ma1.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'tili2') 
    
@svjp.scheduled_job('cron', hour='0', minute='30')
async def sleep():
    path = 'F:/Resources/pcrwarn/那就这样，贵安.mp3'
    msgs = [
        f'已经12点半了哦~你也要早点休息！{R.img("randomimg/ma/ma13.jpg").cqcode}\n',
        f'[CQ:record,file=file:///{path}]'
    ]
    await svjp.broadcast(msgs, 'sleep') 