# **Priconne**
## **基于[**HoshinoBot**](https://github.com/Ice-Cirno/HoshinoBot)的PCR实用小功能**   

### 本模块包含[arena]()，[cherugo]()，[news]()，[gacha]()，[query]()，[comic]()， [horse]()，[login-bonus]()
### [**arena**](HoshinoBot/hoshino/modules/priconne/arena/README.md)，[**news**](HoshinoBot/hoshino/modules/priconne/news/README.md)，[**gacha**](HoshinoBot/hoshino/modules/priconne/gacha/README.md)，[**query**](HoshinoBot/hoshino/modules/priconne/query/README.md)有单独的说明文档 ，故不在此README里重复说明

- ## cherugo
切噜语（ちぇる語, Language Cheru）转换  

定义:  
    W_cheru = '切' ^ `CHERU_SET`+  
    切噜词均以'切'开头，可用字符集为`CHERU_SET`  
    L_cheru = {W_cheru ∪ `\\W`}*  
    切噜语由切噜词与标点符号连接而成  

- ## comic
官方四格漫画推送(日文)与查阅  
从日服官网下载四格漫画到`Resources/img/priconne/comic/`目录下，若有更新则推送至订阅群

- ## horse
简易模拟赛马  
可以按需要更改`config.json`中内容，与改抽卡模拟调用的池子一样  
icon_unit_960131.png等4个图片放在存放角色图标的文件夹下，即`Resources/img/priconne/unit/`下

- ## login-bonus
模拟登陆签到  
可自行在`login_bonus.py`里变更文本  
`login_bonus.py`第55行需对应图片Resources/img/priconne/kokkoro_stamp.png
```python
await bot.send(ev, f'\nおかえりなさいませ、主さま{R.img("priconne/kokkoro_stamp.png").cqcode}\n{present}を獲得しました\n私からのプレゼントです\n主人今天要{todo}吗？', at_sender=True)
```
