from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NUM_AND_LETTER = State()
    GET_DAY = State()
    GET_SCHEDULE = State()