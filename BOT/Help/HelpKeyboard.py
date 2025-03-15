from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

hp_kbR = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Расскажи шутку🤓"),KeyboardButton(text="Расскажи курс валют💵")],
    [KeyboardButton(text="Мой профиль⚙️"),KeyboardButton(text="Помощь🤖")],
    [KeyboardButton(text="Настройки подписки🐍"),KeyboardButton(text="Об авторе👥")],
    [KeyboardButton(text="Обновить клавиатуру⌨️")]
],resize_keyboard=True,input_field_placeholder="Пожалуйста выберите опцию...")

hp_kbI = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Мой Telegram🔔", url="https://t.me/Lesh_737"),InlineKeyboardButton(text="Мой ютуб🎥",url="https://www.youtube.com/@MaProgrammNotProgramming")]
])