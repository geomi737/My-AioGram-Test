import asyncio

from aiogram.types import Message,CallbackQuery
from aiogram import Router,F,html
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext

from exchangeValues.exchangerateClass import value_state
from exchangeValues.exchangerateReqest import get_values
#exchangerateHandler router - eh_rt
eh_rt = Router()

@eh_rt.message(F.text == "Расскажи курс валют💵")
@eh_rt.message(Command("change"))
async def value_command(message: Message, state: FSMContext):
    await message.reply("Введите нужную валюту.При вводе просим указывать в формате трех букв,как EUR или RUB.\nВалюта будет сравниваться только с долларом!")
    await state.set_state(value_state.vwaiting)
    
@eh_rt.message(value_state.vwaiting)
async def value_textChoice(message: Message, state: FSMContext):
    await state.update_data(value = message.text)
    data = await state.get_data()
    await message.answer(await get_values(data["value"]))
    await state.set_state()