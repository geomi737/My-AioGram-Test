#Импорты
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command,CommandStart
from aiogram import F

from Database.Requests import message_increment

#Создание роутера
mt_rt = Router()

#Счетчик сообщений
@mt_rt.message()
async def take_message(message: Message):
    print(message.text)
    await message_increment(message.from_user.id)
    
    