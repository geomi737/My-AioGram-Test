import asyncio

from aiogram.types import Message,CallbackQuery
from aiogram import Router,F,html
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.types import ReplyKeyboardRemove

from Database.Requests import initialize_user,profile_info

from Help.HelpKeyboard import hp_kbR,hp_kbI

from datetime import datetime

#hh_rt - help_handlers router
hh_rt = Router()

@hh_rt.message(CommandStart())
async def start_command(message: Message):
    try:
        await initialize_user(message.from_user.id,message.from_user.username)
        await message.answer_photo('https://m.media-amazon.com/images/I/71m9fX5HlkL._UF1000,1000_QL80_.jpg',f"Здравствуй,{message.from_user.username},"+
                         "я бот.Но я не просто бот,я бот предназначеный для привязки к базе данных.",reply_markup=hp_kbR)
    except AttributeError:
        await initialize_user(message.from_user.id,"NonameHASH128125125152612")
        await message.answer(f"Здравствуй,я не смог получить твоё имя,но неважно."+
                         "я бот.Но я не просто бот,я бот предназначеный для привязки к базе данных.",reply_markup=hp_kbR)

@hh_rt.message(F.text == "Помощь🤖")
@hh_rt.message(Command("help"))
async def help_command(message: Message):
    #нужно привязать клавиатуру ко всем возможностям
    await message.answer("/change - Курс валют относительно доллара\n/joke - Случайная шутка (обычно КРАЙНЕ тупорылая).\n"
                         + "/start - выводит кнопочки :0")


@hh_rt.message(F.text == "Об авторе👥")
@hh_rt.message(Command("about"))
async def about_author(message: Message):
    await message.answer("Привет.Я работаю над этим ботом для гитхаб,так что про себя ничего говорить не хочу."+
                    "\nНо тот кому я дам этого бота протестировать,уже обо всём вкурсе", reply_markup=hp_kbI)
    
@hh_rt.message(F.text == "Мой профиль⚙️")
@hh_rt.message(Command("profile"))
async def message_cSayer(message: Message):
    UserInfo = await profile_info(message.from_user.id, "User Info")
    SubInfo = await profile_info(message.from_user.id, "Sub Info")
    
    # Базовый профиль без информации о подписке
    base_profile = (
        f"Ваш профиль:\n"
        f"ID:{UserInfo.id}\n"
        f"Username:{UserInfo.username}\n"
        f"TelegramID:{UserInfo.tg_id}\n"
        f"Написано сообщений:{UserInfo.message_counter}"
    )
    
    # Проверяем наличие информации о подписке
    if SubInfo != None and SubInfo != "Отсутствие данных!":
        try:
            SubInfo_Date_ForUser = SubInfo.subscription_date.strftime("%d.%m.%Y") if SubInfo.subscription_date else "Не указана"
            SubInfo_forUser = "Активна" if SubInfo.subscription_activity else "Неактивна"
            
            full_profile = (
                f"{base_profile}\n\n"
                f"Информация о подписке:\n"
                f"Активность: {SubInfo_forUser}\n"
                f"Дата окончания: {SubInfo_Date_ForUser}"
            )
            await message.reply(full_profile)
        except AttributeError:
            # В случае ошибки с атрибутами выводим базовый профиль
            await message.reply(base_profile)
    else:
        # Если нет информации о подписке, выводим базовый профиль
        await message.reply(base_profile)
        
@hh_rt.message(F.text == "Обновить клавиатуру⌨️")
@hh_rt.message(Command("reboot_keyboard"))
async def reload_keyboard(message: Message):
    await message.answer("Клавиатура обновлена!",reply_markup=hp_kbR)