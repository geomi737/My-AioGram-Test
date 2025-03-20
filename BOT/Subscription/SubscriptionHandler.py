import asyncio

from aiogram.types import Message,CallbackQuery
from aiogram import Router,F,html
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.types import ReplyKeyboardRemove

import Subscription.SubscriptionKeyboard as sk

from Database.Requests import add_subscription,subscription_cancel,renew_sub_request,check_sub

sh_rt = Router()

@sh_rt.message(Command("sub_settings"))
@sh_rt.message(F.text == 'Настройки подписки🐍')
async def connect_subscription(message: Message):
    await message.answer("Выберите действие:",reply_markup=sk.subMenu_kb)
    
@sh_rt.callback_query(F.data == 'buy_subscription')
async def option_CONNECT(callback: CallbackQuery):
    await callback.answer("Выбор длительности")
    await callback.message.edit_text("Выберите длительность:",reply_markup = sk.subDation_kb)
    
@sh_rt.callback_query(F.data == 'days7')
async def days7_connect(callback: CallbackQuery):
    result = await add_subscription(callback.from_user.id,7)
    
    if result == 'Error: Не найден пользователь':
        await callback.answer(text="Ошибка установления подписки", show_alert=True)
    elif result == 'Error: Подписка уже есть':
        await callback.answer(text="Подписка уже есть", show_alert=True)
    elif result == 'SUCCESS!':
        await callback.answer(text="Подписка установлена", show_alert=True)
        await callback.message.edit_text("Подписка установлена")
        
@sh_rt.callback_query(F.data == 'days14')
async def days14_connect(callback: CallbackQuery):
    result = await add_subscription(callback.from_user.id,14)
    
    if result == 'Error: Не найден пользователь':
        await callback.answer(text="Ошибка установления подписки", show_alert=True)
    elif result == 'Error: Подписка уже есть':
        await callback.answer(text="Подписка уже есть", show_alert=True)
    elif result == 'SUCCESS!':
        await callback.answer(text="Подписка установлена", show_alert=True)
        await callback.message.edit_text("Подписка установлена")
        
@sh_rt.callback_query(F.data == 'days30')
async def days30_connect(callback: CallbackQuery):
    result = await add_subscription(callback.from_user.id,30)
    
    if result == 'Error: Не найден пользователь':
        await callback.answer(text="Ошибка установления подписки", show_alert=True)
    elif result == 'Error: Подписка уже есть':
        await callback.answer(text="Подписка уже есть", show_alert=True)
    elif result == 'SUCCESS!':
        await callback.answer(text="Подписка установлена", show_alert=True)
        await callback.message.edit_text("Подписка установлена")
        
@sh_rt.callback_query(F.data == 'cancel_subscription')
async def sub_cancel(callback: CallbackQuery):
    result = await subscription_cancel(callback.from_user.id)
    if result == 'Error: Не найден пользователь':
        await callback.answer(text="Ошибка,вы не найдены в базе данных", show_alert=True)
    elif result == 'Error: Не найдена подписка':
        await callback.answer(text="Ошибка,не найдена подписка",show_alert=True)
    elif result == "Error: Подписка неактивна":
        await callback.answer(text="Подписка уже неактивна",show_alert=True)
    elif result == 'SUCCESS!':
        await callback.answer(text="Успешно!",show_alert=True)
        
@sh_rt.callback_query(F.data == 'renew_subscription')
async def renew_sub(callback: CallbackQuery):
    result = await renew_sub_request(callback.from_user.id)
    
    if result == 'Error: Не найден пользователь':
        await callback.answer(text="Ошибка,вы не найдены в базе данных", show_alert=True)
    elif result == 'Error: Не найдена подписка':
        await callback.answer(text="Ошибка,не найдена подписка",show_alert=True)
    elif result == 'Error: Подписка неактвна':
        await callback.answer(text="Приобретите подписку,для начала",show_alert=True)
    elif result == "Error: Подписка активна более 3 следующих дней":
        await callback.answer(text="Ваша подписка всё еще активна более 3 дней,попробуйте позже",show_alert=True)
    elif result == 'SUCCESS!':
        await callback.answer(text="Успешно!",show_alert=True)
        
@sh_rt.message(Command("subscription_command"))
async def sub_only(message: Message):
    result = await check_sub(message.from_user.id)

    if result == False:
        await message.answer("У вас нет подписки")
        
    elif result == True:
        await message.answer("Команда выполнена")