# **Aichat**
## **腾讯AI回复功能** 
### 利用tx智能闲聊接入Bot 。本模块默认关闭，开启后可发送 `开启对线` 和 `关闭对线` 调整AI回复概率（100%和10%）
### 在 第105行 可以调整概率下限
```python
@sv.on_message('group')
async def ai_reply(bot, context):
    if switch.gpid not in g_open_groups and switch.gpid!= 0:
            if not random.randint(1,100) <= 10:#拙劣的概率开关
                return
```