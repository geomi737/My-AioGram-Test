import asyncio

from aiogram.types import Message,CallbackQuery
from aiogram import Router,F,html
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

from Jokes.JokeRequest import get_joke

#jj_rt = joke router
jj_rt = Router()

@jj_rt.message(F.text == "Расскажи шутку🤓")
@jj_rt.message(Command("joke"))
async def joke_handler(message: Message):
    await message.answer(await get_joke())