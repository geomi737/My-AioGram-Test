#Импорты
from dotenv import load_dotenv
import asyncio
from os import getenv
import logging
import sys

from Jokes.JokeHandler import jj_rt
from Help.HelpHandlers import hh_rt
from exchangeValues.exchangerateHandler import eh_rt
from messageTaker import mt_rt

from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message

from Database.models import create_new_table

#Запуск логирования и получение токена из файла .env
logging.basicConfig(level=logging.INFO,stream=sys.stdout)

load_dotenv("TOKEN.env")

#Функция объявления и запуска бота и диспетчера
async def main():
    dp = Dispatcher()
    bot = Bot(token=getenv("TOKEN"))
    dp.include_routers(hh_rt,jj_rt,eh_rt,mt_rt)
    
    await dp.start_polling(bot)

#Проверка на запуск main() из файла main.py
if __name__ == "__main__":
    try:
        asyncio.run(main())
        #создание новой таблицы
        asyncio.run(create_new_table())
        #Надпись при отключении
    except KeyboardInterrupt:
        print("Shutting Down")
