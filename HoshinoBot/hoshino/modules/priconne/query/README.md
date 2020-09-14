# **Priconne-Query**
## **基于[**HoshinoBot**](https://github.com/Ice-Cirno/HoshinoBot)的Rank表快捷查询功能。**   
## 不仅是Rank表，还有更多攻略资料可供查阅
### 本模块包含[miner]()，[whois]()，[query]()
- ## miner
竞技场矿场余矿查询，支持多个指令前缀
```python
sv.on_prefix(('挖矿', 'jjc钻石', '竞技场钻石', 'jjc钻石查询', '竞技场钻石查询'))
```
- ## whois
角色别称查询，支持指令前缀和后缀
```python
sv.on_suffix('是谁')
sv.on_prefix('谁是')
```
- ## query
PCR快捷资料查询，可以查阅的内容有：**RANK表**，**资料网站**，**攻略链接**，**黄骑充电表**，**注音文字**
```python
sv.on_fullmatch(('rank表', 'Rank表', 'RANK表'))
sv.on_fullmatch(('pcr速查', 'pcr图书馆', '图书馆'))
sv.on_fullmatch(('bcr速查', 'bcr攻略'))
sv.on_fullmatch(('一个顶俩', '拼音接龙', '韵母接龙'))
sv.on_fullmatch(('其他资料', '其他攻略', '更多资料', '更多攻略', '其它资料', '其它攻略'))
```