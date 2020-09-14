# **Groupmaster**
## **基于[HoshinBot](https://github.com/Ice-Cirno/HoshinoBot)的轻量群管功能**
## 本模块包含[group_notice]()，[join_approve]()，[random_repeater]()，[sleeping_set]()

- ## group_notice
### 进群/退群通知，可在`hoshino/config/groupmaster.py`里自定义入群欢迎语
```python
increase_welcome = {
    "default": "欢迎入群！我是本群bot，您可以发送【使用说明】和【指令表】查看我的说明哦！",
    1000000: "欢迎新群员！我是本群bot，您可以发送【使用说明】和【指令表】查看我的说明哦！",
}
```
### 在本文件第9行自定义退群通知
```python
@sv1.on_notice('group_decrease.leave')
async def leave_notice(session: NoticeSession):
    await session.send(f"{session.ctx['user_id']}离开了本群。")
```

- ## join_approve
### 加群审批，当加群验证信息包含特定词后放行，可在`hoshino/config/groupmaster.py`里自定义验证词
```python
join_approve = {
    1000000: {
        "keywords": ["入群暗号"],
        "reject_when_not_match": True
    },
}
```

- ## random_repeater
### 随机复读功能，可复读图片，在本文件第9行更改复读概率
```python
PROB_A = 1.4
```
> 不复读率 随 复读次数 指数级衰减  
从第2条复读，即第3条重复消息开始有几率触发复读  
PROB_A 设为一个略大于1的小数，最好不要超过2，建议1.6  
复读概率计算式：p_n = 1 - 1/PROB_A^n  
递推式：p_n+1 = 1 - (1 - p_n) / PROB_A  

- ## sleeping_set
### 睡眠套餐(禁言)功能，可自定义触发词和禁言时长，单位为秒(s)
```python
@sv.on_fullmatch(('睡眠套餐', '休眠套餐', '精致睡眠', '来一份精致睡眠套餐'))
async def sleep_8h(bot, ev):
    await util.silence(ev, 8*60*60, skip_su=False)
    # 禁言时长为8*60*60=8小时，skip_su配置是否忽略主人
```