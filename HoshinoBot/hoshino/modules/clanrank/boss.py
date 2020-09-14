# 此部分来自艾琳佬，感谢艾琳佬，赞美艾琳佬
import math

bossData = {
    'scoreRate': [
        [1, 1, 1.1, 1.1, 1.2],
        [1.2, 1.2, 1.5, 1.7, 2],
    ],
    'hp': [6000000, 8000000, 10000000, 12000000, 20000000],
    # 国服无多周目差别
    'max': 2,
}

def calc_hp(hp_base: int):
    zm = 1
    king = 1
    cc = 0.0
    remain = 0.0
    damage = 0
    remainHp = 0.0
    remainPer = 0.0

    while True:
        nowZm = bossData['max'] - 1 if zm > bossData['max'] else zm - 1
        cc += bossData['scoreRate'][nowZm][king - 1] * bossData['hp'][king - 1]
        if cc > hp_base:
            cc -= bossData['scoreRate'][nowZm][king - 1] * bossData['hp'][king - 1]
            remain = (hp_base - cc) / bossData['scoreRate'][nowZm][king - 1]
            damage += remain
            remainPer = 1.0 - remain / bossData['hp'][king - 1]
            remainHp = bossData['hp'][king - 1] - remain
            break
        damage += bossData['hp'][king - 1]
        if king == 5:
            zm += 1
            king = 1
            continue
        king += 1
    remainPer *= 100
    bdk = bossData['hp'][king - 1]
    return f'{zm}周目{king}王 [{math.floor(remainHp)}/{bdk}]  {round(remainPer, 2)}%'

