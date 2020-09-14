try:
    import ujson as json
except:
    import json
import requests



async def get_weather_of_city(city: str) -> str:
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
    data_json = requests.get(url).json()
    if 'desc' in data_json:
        if data_json['desc'] == "invilad-citykey":
            return "抱歉没有搜索到结果呢(╥﹏╥)"
        elif data_json['desc'] == "OK":
            w_type = data_json['data']['forecast'][0]['type']
            w_max = data_json['data']['forecast'][0]['high'][3:]
            w_min = data_json['data']['forecast'][0]['low'][3:]
            fengli = data_json['data']['forecast'][0]['fengli'][9:-3]
            ganmao = data_json["data"]["ganmao"]

            repass = f'{city}的天气是' + w_type + "天\n最高温度:" + w_max + "\n最低温度:" + w_min + "\n风力:" + fengli + "\n" + ganmao

            return repass
