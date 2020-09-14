# Mirai-Bot-Setup

*基于[Mirai](https://github.com/mamoe/mirai)，[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)，[Yobot](http://yobot.win/)的**QQ机器人搭建指南***

请注意：本指南**并非**官方文档，写此指南的目的是方便编程**初学者**或毫无经验的**小白**快速上手搭建自己的bot

**感谢[Mirai](https://github.com/mamoe/mirai)项目 ，[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)项目，[Yobot](https://github.com/pcrbot/yobot)项目，[cqhttp-mirai](https://github.com/yyuueexxiinngg/cqhttp-mirai) 插件和 众多[bot插件](https://www.pcrbot.com/) 的开发者们！**

**本指南具有时效性，请注意。**


# 写在前面

参照本指南引导，个人搭建者无需编程知识即可快速搭建bot，但仍建议您了解一些有关**Python，Java, Kotlin等**的基础知识。

善用[Baidu](https://www.baidu.com/), [Bing](https://cn.bing.com/), [Google](http://www.google.cn/)等搜索引擎能帮助您更快上手

若对自己搭建的bot**不完全了解**各项参数，指令等含义，请**不要**将bot用于出租

## 简介

- **Mirai:** 是一个在全平台下运行，提供 QQ Android 协议支持的高效率机器人库

- **HoshinoBot:** 基于 [nonebot](http://nonebot.cqp.moe) 框架，开源、无公害、非转基因的QQ机器人。

- **Yobot:** 为[公主连结Re:dive](https://game.bilibili.com/pcr/)公会战设计的辅助机器人，能够帮助公会战管理者提供自动化管理服务。

- **CQHTTP-MIRAI:** 为Mirai移植的CQHTTP插件以兼容基于CQHTTP API开发的应用

- **QQ机器人的运作方式:** 简单来说，Mirai相当于一个下载了QQ的手机，而cqhttp-mirai是连接的WIFI信号，HoshinoBot，Yobot则是这个手机后面打字的人。

本指南将引导您将HoshinoBot和Yobot利用cqhttp-mirai缝合到Mirai上。


## 功能介绍

根据本指南部署完成的bot应具有以下功能：

- **基于腾讯AI闲聊的智能闲聊**  [aichat]()
- **模拟群空调运行**  [aircon]()
- **公会人员公开黑名单**    [blacklist]()
- **Bot轻量语言库**    [botchat]()
- **公主连结日程表查阅推送**    [calendar]()
- **实时查询公会排名**  [clanrank]()
- **模拟掷骰子**  [dice]()
- **爆裂魔法**  [explosion]()
- **无损音乐资源搜索**  [flac]()
- **文章/表情包 生成器**    [generator]()
- **猜角色小游戏**    [guess]()
- **整点时报**  [hourcall]()
- **定时提醒**  [pcrwarn]()
- **公会战管理**    [clanbattle]()
- **PCR实用小功能** - 包含**官方四格漫画推送(日文)与查阅**，**公主连结R官方新闻推送**，**竞技场作业查询**，**简易模拟赛🐎**，**模拟抽卡** ，**Rank表快捷查询**  [priconne]()
- **你问我答**  [QA]()
- **公会战报告图生成**  [report]()
- **模拟俄罗斯转盘**    [russian]()
- **p站搜**   [pixiv]()
- **steam商店查询**    [steam]()
- **群老婆**    [laopo]()
- **群内点歌**    [music]()
- **日语词典**    [japanese]()
- **天气查询**    [weather]()
- **随机涩图**  [setu]()
- **识别图片来源**  [search]()
- **Visual YouTuber运势签** [vortune]()
- **短篇网抑云语录**    [wcloud]()

~~还有部分隐藏功能~~    
Bot 的功能繁多，可根据自身需要控制开关，在群聊中发送 `lssv` 即可查看各功能模块的启用状态，使用以下命令进行控制：

```
启用 service-name
禁用 service-name
```
为防止单条消息过长，每项功能的指令说明分别显示。使用以下命令可以查看各项功能的说明：

```
service-name帮助
```

# 准备工作

**本指南面向无编程基础或刚入门的萌新，故推荐使用具有图形界面，对新手操作友好的Windows服务器来进行部署**

- 准备一台Windows系统的服务器（或个人本地电脑）

- 登录服务器控制台，在防火墙/安全组等界面，放通**80，8080，8090，9222**端口
> 以腾讯云为例：  
  在 云服务器 - 安全组 - 安全组规则 里 添加 入站与出站规则

> 以阿里云为例：  
  在 云服务器 - 防火墙 里 添加规则

> 以本地个人电脑为例：  
  在 控制面板 - 系统和安全 - Windows Defender 防火墙 - 高级设置 里 添加 入站规则 与 出站规则  
  不建议运行在本地个人电脑上。

- 在任意位置打开任意一个文件夹，点击左上方的`查看`-`显示/隐藏`页面中，勾选`文件扩展名`

- （可选）使用 IE 或自行安装其他浏览器，用Bot 的QQ号登录网页[QQ安全中心](https://aq.qq.com/cn2/index)并保持登录至少一周。~~(即使不执行此步骤，Bot 仍然可正常搭建运行，但部分群聊消息可能会被tx吞，且异地登录有冻结风险)~~

# 部署步骤

### Windows 部署

1. 安装下列软件/工具

    - Python ：https://www.python.org/downloads/windows/
    - Git ：https://git-scm.com/download/win
    - Java ：https://www.java.com/zh_CN/download/win10.jsp
    - Notepad++ ：https://notepad-plus-plus.org/downloads/

    > 部分网页国内网络可能访问缓慢，这里提供已整合好的压缩文件  
    > 百度网盘：**[安装资源整合包](https://pan.baidu.com/s/1HwD-Z0f7msXKXLR0_Bec9Q)**
    > 提取码：***4396***  
    > 以上软件/工具可在整合包里的**backups/software**里找到

2. 在合适的文件目录（例如桌面）新建文件夹并双击打开，点击文件夹左上角的 `文件 -> 打开Windows Powershell`，输入以下命令

    ```powershell
    git clone https://github.com/Soung2279/Mirai-Bot-Setup.git
    ```
    在合适的文件目录（推荐C盘根目录）新建文件夹并重命名为`Resources`  
    将收集到的 图片/语音资源 放入该文件夹，注意文件目录结构
    ```
    应当具有以下路径
    C:\Resources
    C:\Resources\img        总的图片存放位置
    C:\Resources\img\priconne       PCR实用小功能的图片位置
    C:\Resources\img\priconne\comic     PCR实用小功能-4格漫画
    C:\Resources\img\priconne\unit      PCR实用小功能-模拟抽卡角色头像
    C:\Resources\img\priconne\quick     PCR实用小功能-rank表
    C:\Resources\img\setu       涩图
    C:\Resources\gacha      抽卡音效
    C:\Resources\MEGUMIN\explosion      爆裂魔法
    C:\Resources\pcrwarn        定时提醒语音
    ......
    ```
    > 若自行整理资源困难，这里提供已整合好的压缩文件  
    > 百度网盘：**[资源包](https://pan.baidu.com/s/1LKpJ2jOh3XOQSW308TL4bg)**
    > 提取码：***2200***  

3. 运行一次`yobot.exe`, 待弹出的窗口显示完毕后(*显示CTRL + C to quit字样后*)，关闭窗口

4. **修改以下几个文件的配置**

    - 在`yobot_data/yobot_config.json`文件中，将文中这几行语句内容更改为下列示例给出的内容（其他行不用改动，若和示例相同则无须变动。）
    ```json
    {
        "host": "0.0.0.0",
        "port": 9222,
        "public_address": "http://你的服务器公网IP:9222/",
    }
    ```

    - 在`config.txt`文件中，将需要**作为bot的QQ号和密码**输入在第二个 `login` 之后，用 `空格` 分隔
    ```json
    ----------
    login 你的botQQ号 QQ密码
    ```

    - 在`plugins/setting.yml`文件中，将第一行的数字换成**你的bot的QQ号**
    ```yml
   "你的bot的QQ号":
    ```

    - 在`HoshinoBot/hoshino/config/_bot_.py`文件中，将`SUPERUSERS`后的数字改为**你自己的QQ号**，将NICKNAME后的名称更改为**你自定义的名字**，将`RES_DIR`后的路径改为你在**第二步**新建的`Resources`路径
    ```python
    SUPERUSERS = [123456789]
    NICKNAME = '妈', 'xcw'
    RES_DIR = r'C:/Resources/'
    ```

    - 在`HoshinoBot/hoshino/modules/vortun/main.py`文件里，将`absPath`后的路径改为此文件当前的路径（注意用`\\双斜线`分层）
    ```python
    absPath = 'C:\\Mirai-Bot-Setup\\HoshinoBot\\hoshino\\modules\\vortune'
    ```

5. (可选) 在以下文件中填入你自己的APIKEY
   - 在`HoshinoBot/hoshino/modules/aichat/aichat.py`文件里添加腾讯智能闲聊的API （已内置我的API，但建议去[申请](https://ai.qq.com/v1/)一个）
   ```python
   ################
    # 请修改
    app_id = '123456789'
    app_key = 'abcdefghijk'
    ################
   ```

   - 在`HoshinoBot/hoshino/config/priconne.py`文件里添加[竞技场作业网](https://pcrdfans.com/)的API（需要去[申请](https://pcrdfans.com/bot)）
   ```python
   class arena:
    AUTH_KEY = "你的作业网API"
   ```

   - 在`HoshinoBot/hoshino/modules/search-image/picfinder.py`文件里**第15行**添加[SauceNAO识别图片](https://saucenao.com/index.php)的API（需要去[申请](https://saucenao.com/user.php)，已内置了我自己的API，但过多使用可能造成请求额度不够）
   ```python
    api_key="abcdefghijklmn123"#填写你自己的api_key
   ```
   - 在`HoshinoBot/hoshino/modules/pixiv/config.yml`文件中填入你自己的pixiv账号
   ```yml
   pixiv:
   username: '132456789'
   password: '132456789'
   ```
6. 运行`双击安装依赖.bat`，若此过程中有报错信息，请重新运行一次，若仍有报错，请复制报错信息到搜索引擎获得帮助

### 开始使用
运行 `Mirai-Bot-Setup` 下的 `yobot.exe` , `双击运行Mirai.bat` 和 `HoshinoBot` 下的 `双击运行HoshinoBot.bat` 。显示以下字样说明bot启动成功：
#### *双击运行HoshinoBot.bat*
```python
Running on http://127.0.0.1:8090 (CTRL + C to quit)
[2020-09-12 21:19:17,706] Running on 127.0.0.1:8090 over http (CTRL + C to quit)
```
#### *yobot.exe*
```python
yobot[v3.6.4]便携版
初始化完成，启动服务...
Running on https://0.0.0.0:9222 (CTRL + C to quit)
```
#### *双击运行Mirai.bat*
```java
[0m 21:21:55 [INFO] [BOT 你的bot的QQ号] Logging in...[39;49m
[0m 21:21:55 [INFO] [NETWORK] Connected to server msfwifi.3g.qq.com:8080[39;49m
......
[0m 21:21:56 [INFO] [NETWORK] 开始加载好友信息[39;49m
[0m 21:21:56 [INFO] [NETWORK] 开始加载群组列表与群成员列表[39;49m
......
[0m 21:21:57 [INFO] [BOT 你的bot的QQ号] Login successful[39;49m
[0m 21:21:57 [INFO] [Command] 你的bot的QQ号 login successes[39;49m
```

> 若此过程中有报错信息，请复制报错信息到搜索引擎  
> 此过程中常见的报错为资源缺失，请确认**第四步**中修改的`RES_DIR`路径是否正确

在bot所在群聊中发送任意信息，若`双击运行Mirai.bat` 和 `双击运行HoshinoBot.bat`窗口**有反应**，说明bot的HoshinoBot部分**正常**运行中。此时可发送【使用指南】/【指令表】来查看bot的帮助文档。  

在bot所在群聊中发送`version`和`help`，若bot在群聊中有反应，说明bot的Yobot部分**正常**运行中。此时可发送【help】来查看bot的会战文档。

# 更进一步

### · 若Bot 运行正常，可考虑开启更多模块以丰富bot的功能。

### · 在 `HoshinoBot/hoshino/config/_bot_.py` 文件里，将需要开启的模块前面的"`#井号`"删除。各项模块对应的功能可在[**写在前面-功能介绍**]()处查看

### · 若想给Bot 添加更多功能，可以自行收集插件放入 `HoshinoBot/hoshino/modules` 文件夹中。（请仔细阅读该插件的说明文档，某些插件的添加方式有所不同）

### · 若Bot 添加群过多，需要引入授权系统，请启用[**authMS**](https://github.com/pcrbot/authMS)插件。Bot 已内置此插件，请仔细阅读说明文档进行配置。

### · 可自定义的内容

- `modules/botchat/botchat.py`：这是**bot的轻量语言库**，可自行添加语句和回复，源文件里已包含范例。不同bot的人格差异化也基于此体现。

- `modules/explosion/exo.py`：这是**爆裂魔法**，可自行更改日调用上限，也可以自行魔改添加更多语音。

- `modules/generator-image/`：这是**表情包生成器**，可在`meme`里自行添加更多表情包。

- `modules/HELP`：这是Bot 的**帮助文档**，可自行更改文本内容。

- `hoshino/config/hourcall.py`：这是**整点时报**的文本内容，可自行更改，也可自行仿照格式添加。

- `modules/pcrwarn`：这是**定时提醒**，可自行更改提醒时间，提醒内容。

- `modules/priconne/gacha/`：这是**模拟抽卡**，可在`gacha.py`中自行更改抽卡次数日上限，还可在`config.json`中自行更改卡池内容。

- `modules/setu/setu.py`：这是**涩图**，可自行更改日调用上限。

- `modules/wcloud/`：这是**随机网抑云**，可在`nt_words.json`中自行更改语录文本。

# 常见问题

### Q：为什么我的Bot 发不出图片/语音？
### A：请检查资源路径`RES_DIR`是否设置正确，目录`Resources`下该图片/语音是否存在  

### Q：为什么我的Bot 没有反应？
### A：请查看窗口显示的日志。  
- #### 若日志显示正常，请查看在[**准备工作**]()步骤中是否放通端口。
- #### 若日志有报错信息，请复制报错信息到搜索引擎解决。
- #### 若日志无反应，请在该窗口输入回车`(按下Enter键)`，查看日志是否有反应。若日志仍无反应，请查看在[**部署步骤 - 4.修改以下几个文件的配置**]()中的文件是否正确配置
- #### 若端口已经放通，请尝试其它指令；若部分指令有回应，说明bot 正常运行中，只是部分消息被tx吞了。若所有指令都无回应，请重新运行`双击安装依赖`
- #### 若所有方式都无法让Bot 做出反应，请尝试重新部署Bot。

### Q：Bot 的权限是怎么设定的？
- ### A：基于HoshinoBot的功能，设定主人为**最高**权限`priv.SUPERUSER`，群主为仅次于主人的第二权限`priv.OWNER`，群管理为更次一等的权限`priv.ADMIN`，群员为最低权限`priv.NORMAL`。(黑/白名单不考虑在内) 主人可以在`_bot_.py`里设定多个 
- ### A：而基于Yobot的功能，需要在面板中单独设定群员`公会战管理员`和`成员`，默认群员为`成员`，`公会战管理员`可以设置**多个**，但`主人`只能设定**一个**

### Q：有什么其他的Bug吗？
### A：目前使用的`cqhttp-mirai-0.2.3-embedded-all`插件发送的语音文件仅支持.amr/mp3，且 `.mp3` 在移动端QQ将错误显示时长，在PC端无法播放

### Q：以后的更新维护？
### A：您可以自行访问[Mirai](https://github.com/mamoe/mirai)项目 ，[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)项目，[Yobot](https://github.com/pcrbot/yobot)项目，[cqhttp-mirai](https://github.com/yyuueexxiinngg/cqhttp-mirai) 插件和 众多[bot插件](https://www.pcrbot.com/) 来进行更新。

### Q：还有什么注意事项？
### A：请勿滥用Bot。

# 最后

### 本人非专业程序员，如本篇指南有错误，请及时告知我。
### 本篇指南搭载的Bot 模块 均根据本人喜好进行取舍，世面上还有很多非常优秀的Bot 插件，请自行探寻。

## 鸣谢

### 骨干部分

**HoshinoBot**：https://github.com/Ice-Cirno/HoshinoBot  作者：[@Ice-Cirno](https://github.com/Ice-Cirno)

**Yobot**：http://yobot.win/  作者：[@yuudi](https://github.com/yuudi)

**Mirai**：https://github.com/mamoe/mirai  作者：[@Mamoe Technologies
](https://github.com/mamoe)  

**cqhttp-mirai**：https://github.com/yyuueexxiinngg/cqhttp-mirai  作者：[@yyuueexxiinngg](https://github.com/yyuueexxiinngg)

### 插件部分

- [**Dihe Chen**](https://github.com/Chendihe4975)  
- [**var**](https://github.com/var-mixer)  
- [**xhl6699**](https://github.com/xhl6666)  
- [**Watanabe-Asa**](https://github.com/Watanabe-Asa)  
- [**-LAN-**](https://github.com/laipz8200)  
- [**Cappuccilo**](https://github.com/Cappuccilo)  
- [**yuyumoko**](https://github.com/yuyumoko)  
- [**H-K-Y**](https://github.com/H-K-Y)  
- [**ZhouYuan**](https://github.com/zyujs)  
...

### 资源部分

**干炸里脊资源站**: https://redive.estertion.win/

**公主连结Re: Dive Fan Club - 硬核的竞技场数据分析站**: https://pcrdfans.com/

**Pcrbot - pcrbot相关仓库**: https://www.pcrbot.com/


###   本项目基于[GNU通用公共授权3.0](http://www.gnu.org/licenses/) 开源