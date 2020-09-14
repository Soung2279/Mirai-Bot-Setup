# **Explosion**
## **爆裂魔法**
### **和惠惠一起每天打一发「Explosion」吧！** 
### 注意：语音文件需放在`C:/Resources/MEGUMIN/explosion/`下，建议使用整合的资源包    
### （若自定义语音文件夹则需修改`exo.py`文件里的路径）
```python
@sv.on_fullmatch(('爆裂魔法', '爆烈魔法', '暴烈魔法', 'EXPLOSION'))
async def exosend(bot, ev):
    uid = ev['user_id']
    if not _nlmt.check(uid):
        await bot.send(ev, EXCEED_NOTICE, at_sender=True)
        return
    if exo_switch:
        r = random.choice([a, b, c, d, e, f, g, h, i, j])
        print(r)
        if r == '1':
            uid = ev['user_id']
            _nlmt.increase(uid)
            path = 'C:/Resources/MEGUMIN/explosion/施法吟诵1.mp3'  #修改为你的自定义语音文件目录
            await bot.send(ev, f'[CQ:record,file=file:///{path}]')
            await bot.send(ev, text1)
```