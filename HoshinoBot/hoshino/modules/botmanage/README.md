# **BotManage**
## **Bot 服务管理**
## 包含**邀请入群提示**，**被踢出群提示**，**服务列表**，**控制开关**
## 包含[broadcast]()，[feedback]()

- ## brocast
### 群广播功能，将文字/图片 广播至Bot 所在的每一个群
### 支持多个前缀，仅主人可用
```python
sucmd('broadcast', aliases=('bc', '广播'))
```
- ## feedback
### 反馈信息功能，将文字/图片 反馈至Bot 主人
### 支持多个前缀，每日有两次上限
```python
_max = 2
......
sv.on_prefix(('来杯咖啡', '反馈信息', '上报信息'))
......
```