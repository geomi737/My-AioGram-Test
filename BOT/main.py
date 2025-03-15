from dotenv import load_dotenv
import asyncio
from os import getenv
import logging
import sys

from Jokes.JokeHandler import jj_rt
from Help.HelpHandlers import hh_rt
from ExchangeValues.exchangerateHandler import eh_rt
from messageTaker import mt_rt
from Subscription.SubscriptionHandler import sh_rt

from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message

from Database.models import create_new_table

import alembic


logging.basicConfig(level=logging.INFO,stream=sys.stdout)
load_dotenv("TOKEN.env")

async def main():
    await create_new_table()    
    dp = Dispatcher()
    bot = Bot(token=getenv("TOKEN"))
    
    print("Добавляю роутеры...")
    dp.include_routers(hh_rt,jj_rt,eh_rt,sh_rt,mt_rt)
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting Down")
