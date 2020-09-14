# **Pcrwarn**
## **定时提醒**
### **默认提醒的时间为 每6小时的买药，每天的任务体力，竞技场结算前20分钟，日常任务刷新时间，您可以自行修改，以下给出范例：** 
```python
@svbl.scheduled_job('cron', hour='6') #早上6点
async def day1_reminder():
    path = 'C:/Resources/pcrwarn/要感谢我哦.mp3'  #设置语音提醒路径
    msgs = [
        f'游戏商店内可以买经验药水了哦！\n快和我一起速速升级成为本群最强的骑士君吧！\n(1/4){R.img("yao.jpg").cqcode}\n',   #自定义文本，`R.img配置附带图片`
        f'[CQ:record,file=file:///{path}]'  #发送语音
    ]
    await svbl.broadcast(msgs, 'day1_reminder')
```