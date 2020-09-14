# **Priconne-News**
## **基于[**HoshinoBot**](https://github.com/Ice-Cirno/HoshinoBot)的公主连结Re:dive官方新闻推送功能。**   
## - 以下是原说明文档 -
### Ref: https://github.com/yuudi/yobot/blob/master/src/client/ybplugins/spider
### GPLv3 Licensed. Thank @yuudi for his contribution!
## - -
### 本模块从[台服官网](http://www.princessconnect.so-net.tw/news/)，[B服官网](game.bilibili.com/pcr/news.html)定时爬取新闻。
### 本模块在`lssv`中列出的服务名为`news-tw`和`news-bili`，其中`news-tw`默认关闭。群管理及以上权限可控制开关
```python
svtw = Service('news-tw', visible=True, manage_priv=priv.ADMIN, enable_on_default=False)
svbl = Service('news-bili', visible=True, manage_priv=priv.ADMIN, enable_on_default=True)
```