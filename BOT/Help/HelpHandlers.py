#Импортируем
import asyncio

from aiogram.types import Message,CallbackQuery
from aiogram import Router,F,html
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.types import ReplyKeyboardRemove

from Database.Requests import initialize_user,profile_info

from Help.HelpKeyboard import hp_kbR,hp_kbI

#Объявляем роутер
hh_rt = Router()

#Создаем обработчик для команды /start
@hh_rt.message(CommandStart())
async def start_command(message: Message):
    await initialize_user(message.from_user.id,message.from_user.username)
    await message.answer(f"Здравствуй,{message.from_user.username},"+
                         "я бот.Но я не просто бот,я бот предназначеный для привязки к базе данных.",reply_markup=hp_kbR)

#Создаем обработчик для команды /help
@hh_rt.message(F.text == "Помощь🤖")
@hh_rt.message(Command("help"))
async def help_command(message: Message):
    #нужно привязать клавиатуру ко всем возможностям
    await message.answer("/change - Курс валют относительно доллара\n/joke - Случайная шутка (обычно КРАЙНЕ тупорылая).\n"
                         + "/start - выводит кнопочки :0")

#Обработчики текста
@hh_rt.message(F.text == "Об авторе👥")
async def about_author(message: Message):
    await message.answer("Привет.Я работаю над этим ботом для гитхаб,так что про себя ничего говорить не хочу."+
                    "\nНо тот кому я дам этого бота протестировать,уже обо всём вкурсе", reply_markup=hp_kbI)
    
@hh_rt.message(F.text == "Мой профиль⚙️")
async def message_cSayer(message: Message):
    info = await profile_info(message.from_user.id)
    await message.reply(f"Ваш профиль:\nID:{info.id}\nUsername:{info.username}\nTelegramID:{info.tg_id}\nНаписано сообщений:{info.message_counter}")
