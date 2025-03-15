import requests
import json


async def get_joke():
    url = ("http://rzhunemogu.ru/RandJSON.aspx?CType=1")

    responce = requests.get(url)
    #responce.encoding = "windows-1251"

    if responce.status_code == 200:
        joke = responce.text
        joke = joke.replace('{"content":"', "").replace('"}', "")
        return joke
    else:
        return "Загрузка не удалась...возможная проблема - повреждение API"