# **Guess-icon**
## **猜角色小游戏-根据头像局部来猜角色**
### 可在本文件自定义如下参数
```python
PIC_SIDE_LENGTH = 25 # 见下段
ONE_TURN_TIME = 20 # 定义每次猜题时长
BLACKLIST_ID = [1072, 1908, 4031, 9000] # 排除角色，ID可在 `_pcr_data.py`里查看
```

```python
    img = c.icon.open()
    left = math.floor(random.random()*(129-PIC_SIDE_LENGTH))
    upper = math.floor(random.random()*(129-PIC_SIDE_LENGTH))
    cropped = img.crop((left, upper, left+PIC_SIDE_LENGTH, upper+PIC_SIDE_LENGTH))
```
