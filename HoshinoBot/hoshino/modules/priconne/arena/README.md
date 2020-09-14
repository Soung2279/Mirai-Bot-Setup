# **Priconne-Arena**
## **基于[**HoshinoBot**](https://github.com/Ice-Cirno/HoshinoBot)的竞技场作业查询功能**   
## - 以下是原说明文档 -
### 本模块基于 0皆无0（NGA uid=60429400）dalao的[PCR姬器人：可可萝·Android](https://bbs.nga.cn/read.php?tid=18434108)，移植至nonebot框架而成。

### 重构 by IceCoffee

### 源代码的使用已获原作者授权。
## - -
### 本模块从[竞技场作业网](https://pcrdfans.com)中获取信息。
### 本模块在`lssv`中列出的服务名为`arena`，默认启用。群管理及以上权限可控制开关
### 使用 `b怎么拆` 或 `台怎么拆` 可以按服务器过滤作业
```python
sv = Service('arena', visible=True, manage_priv=priv.ADMIN)
......
aliases = ('怎么拆', '怎么解', '怎么打', '如何拆', '如何解', '如何打', 'jjc查询')
aliases_b = tuple('b' + a for a in aliases) + tuple('B' + a for a in aliases)
aliases_tw = tuple('台' + a for a in aliases)
aliases_jp = tuple('日' + a for a in aliases)
......
```