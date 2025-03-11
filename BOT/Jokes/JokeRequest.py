#Импортируем библиотеки
import requests

#Создаем функцию для получения шутки
async def get_joke():
    #Ссылка на API с шутками
    url = ("http://rzhunemogu.ru/RandJSON.aspx?CType=1")

    #Получаем ответ от API
    responce = requests.get(url)
    
    #Проверям на успешность получения и выдаем
    if responce.status_code == 200:
        joke = responce.text
        joke = joke.replace('{"content":"', "").replace('"}', "")
        return joke
    else:
        return "Загрузка не удалась...возможная проблема - повреждение API"