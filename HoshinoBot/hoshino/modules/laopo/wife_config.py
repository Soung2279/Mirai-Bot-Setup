import random
from .random_config_index import *
import requests
import json
import os


async def write(wife_list):
    if len(wife_list.user_wife_list) > 0:
        with open('index.json', 'w+', encoding='utf-8') as f:
            src = '['
            for wife in wife_list.user_wife_list:
                date = {'name': wife.name,
                        'age': wife.age,
                        'husband': wife.husband,
                        'ouBai': wife.ouBai,
                        'height': wife.height,
                        'weight': wife.weight,
                        'character': wife.Character,
                        'bud': wife.bud,
                        'isMerry': wife.isMerry,
                        'liking': wife.liking,
                        'work': wife.work,
                        'race': wife.race}
                if len(wife_list.user_wife_list) - 1 == wife_list.user_wife_list.index(wife):
                    src = src + (json.dumps(date, ensure_ascii=False))
                else:
                    src = src + (json.dumps(date, ensure_ascii=False) + ',\n')
            src = src + (']')
            f.write(src)
            f.close()


class user:
    def __init__(self, id):
        self.id = id
        self.fuckingBoy = 0


class user_list:
    def __init__(self):
        self.user_wife_list = list()
        self.user = list()
        self.all_user = list()
        self.alredyInit = False

    async def add_user(self, wife):
        self.user_wife_list.append(wife)
        self.user.append(wife.husband)
        self.all_user.append(user(wife.husband))


class wife:
    def __init__(self, user):
        self.husband = user

        WorkRandom = random.randint(0, len(work) - 1)
        self.work = work[WorkRandom]

        RaceRandom = random.randint(0, len(race) - 1)
        self.race = race[RaceRandom]

        SurnameRandom = random.randint(0, len(surname) - 1)
        nameRandom = random.randint(0, len(name) - 1)
        self.name = surname[SurnameRandom] + name[nameRandom]

        OuBaiRandom = random.randint(0, len(ouBaiSize) - 1)
        self.ouBai = ouBaiSize[OuBaiRandom]

        CharacterRandom = random.randint(0, len(Character) - 1)
        self.Character = Character[CharacterRandom]

        age = random.randint(16, 24)
        if self.work == '小学生':
            age -= 8
        self.age = age

        high = random.randint(145, 170)
        if age >= 16 and high < 150 and not self.race == '矮人':
            high += 10
        if self.race == '矮人':
            high -= 30
        self.height = str(high)

        weight = random.randint(45, 60)
        self.weight = str(weight)

        bud = random.randint(0, len(mengDian) - 1)
        self.bud = mengDian[bud]

        self.liking = random.randint(0, 30)

        self.isMerry = False
        self.isTalk = False

        self.scence = None

    def get_merry(self):
        if self.liking >= 50 and self.isMerry == False:
            self.isMerry = True
            a = random.randint(0, len(merry_talk) - 1)
            return merry_talk[a]
        elif self.liking < 50:
            return '我对你的好感度还没那么高，我们进展有点太快了'
        elif self.isMerry:
            return '我们已经结婚了'

    def print_wife_index(self):
        index = '\n' + self.name \
                + ":\n年龄:" \
                + str(self.age) \
                + "\n身高：" + self.height \
                + "\n体重:" + self.weight \
                + "\n欧派:" \
                + self.ouBai \
                + "\n种族:" \
                + self.race \
                + "\n职业:" + self.work + '\n性格：' + self.Character + '\n萌点：' + self.bud \
                + "\n当前好感度:" + str(self.liking)
        return index


async def get_love_scence():
    try:
        url = "https://chp.shadiao.app/api.php"
        data = requests.get(url,timeout=3).text
    except:
        data = "今日次数达到上限"
    return data
