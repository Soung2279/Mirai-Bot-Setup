# **Generator-Text**
## **文章生成器，本模块使用原说明文档，来源：[**generator**](https://github.com/pcrbot/cappuccilo_plugins)** 

### 功能

- **营销号 主体/事件/另一种说法**：营销号生成器

> 注意：所有参数都是必填的，**不是**选填，`/`也是必要的
>
> 正确命令示例：营销号 洛洛/白嫖代码/洛洛不会写代码

- **狗屁不通 主题**：狗屁不通生成器

> `data.json`为该生成器的词库，可根据需要自行修改

- **记仇 天气/主题**：记仇表情包生成器

> 同营销号，所有参数都是必填的

- **我(有个|一个|有一个)朋友(想问问|说|让我问问|想问|让我问|想知道|让我帮他问问|让我帮他问|让我帮忙问|让我帮忙问问|问)XXX**：无中生友

> 1. 括号内`|`分隔的内容选填
> 2. xxx为生成图片上要说的话，xxx内的“他”和“她”会自动更换为“我”
> 3. 如果命令后没有艾特任何人，则使用随机头像。`config.json`中可配置在某个群随机的头像范围（不在群内的QQ号也可以），如果某个群没在`config.json`里找到配置，则随机全群成员
> 4. 如果命令后艾特某人，则使用被艾特人的头像

- **日记**：舔狗日记生成器

> `diary_data.json`为该生成器的词库，可根据需要自行修改
>
> 若命令后艾特某人，则使用被艾特人的昵称

### 部署

- 将本项目的`generator`文件夹，放入`hoshino/modules`文件夹下
- 在Releases下载`simhei.ttf`字体文件并放入`generator`文件夹
- 在hoshino的配置文件中添加`generator`模块
- 重启hoshino