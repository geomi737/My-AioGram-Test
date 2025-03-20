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
from NotesCreator.NoteHandler import nt_rt

from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message

from Database.models import create_new_table

from Subscription.SubscriptionScheduler import scheduler

import alembic


logging.basicConfig(level=logging.INFO,stream=sys.stdout)
logging.getLogger("apscheduler").setLevel(logging.WARNING)

load_dotenv("TOKEN.env")

async def main():
    await create_new_table()    
    print("Запускаю шедулер...")
    scheduler.start()
    dp = Dispatcher()
    bot = Bot(token=getenv("TOKEN"))
    
    print("Добавляю роутеры...")
    dp.include_routers(hh_rt,jj_rt,eh_rt,sh_rt,nt_rt,mt_rt)
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting Down")
