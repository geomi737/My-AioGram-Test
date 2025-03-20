from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

note_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Создать",callback_data="Note_Создать"),InlineKeyboardButton(text="Удалить",callback_data="Note_Удалить")],
    [InlineKeyboardButton(text="Просмотреть",callback_data="Note_Просмотреть")]
])

note_back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад",callback_data="Note_Back")]
])