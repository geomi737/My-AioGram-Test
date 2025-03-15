import asyncio

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

subMenu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подключить подписку",callback_data="buy_subscription")],
    [InlineKeyboardButton(text="Продлить текущую подписку",callback_data="renew_subscription")],
    [InlineKeyboardButton(text="Отменить подписку",callback_data="cancel_subscription")]
])

subDation_kb= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="7 дней",callback_data='days7')],
    [InlineKeyboardButton(text="14 дней",callback_data="days14")],
    [InlineKeyboardButton(text="30 дней",callback_data="days30")]
])
