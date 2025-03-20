from aiogram.fsm.state import State,StatesGroup

class Create(StatesGroup):
    notename = State()
    description = State()
    date = State()