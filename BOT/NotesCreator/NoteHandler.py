from aiogram.types import Message,CallbackQuery
from aiogram import Router,F,html
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from NotesCreator import NoteKeyboard
from NotesCreator.FSMClass import Create

from datetime import datetime,timedelta

nt_rt = Router()

@nt_rt.callback_query(F.data == "Note_Back")
@nt_rt.message(Command("my_notes"))
async def user_notes(message: Message, state: FSMContext):
    await message.answer("Выбор опции",reply_markup=NoteKeyboard.note_menu_kb)
    await state.clear()

@nt_rt.callback_query(F.data == "Note_Создать")
async def create_note(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Создание напоминания")
    await state.set_state(Create.notename)
    await callback.message.answer("Введите название записи",reply_markup=NoteKeyboard.note_back_kb)

@nt_rt.message(Create.notename)
async def create_note_name(message: Message, state: FSMContext):
    await state.update_data(notename = message.text)
    await message.answer("Введите описание",reply_markup=NoteKeyboard.note_back_kb)
    await state.set_state(Create.description)
    
@nt_rt.message(Create.description)
async def create_note_descr(message: Message, state: FSMContext):
    await state.update_data(description = message.text)
    await message.answer("Введите дату и время отправки напоминания в формате:\nДД.ММ.ГГ Час.Минута в формате 24 часов",reply_markup=NoteKeyboard.note_back_kb)
    await state.set_state(Create.date)
    
@nt_rt.message(Create.date)
async def create_note_date(message: Message, state: FSMContext):
    try:
         await state.update_data(date = message.text)
         note = await state.get_data()
         note_datecheck = datetime.strptime(note["date"],"%d.%m.%y %H:%M")
         if datetime.now() > note_datecheck:
             await message.answer("Данная дата уже прошла")
         else:
             await message.answer(f"Запись {note["notename"]}] создана!")
             await state.clear()
             
    except Exception:
        await message.answer("Неверное написание даты-времени!")