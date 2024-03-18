from aiogram import Bot, types
from aiogram.types import Message
from core.utils.utils_2 import get_schedule
from core.keyboards.keyboards import start
from aiogram.fsm.context import FSMContext
from core.utils.statestest import StepsForm
from core.keyboards.keyboards import keyboard_days_of_week, keyboard_yes_no
import emoji


async def cmd_start_kb(message: Message, bot:Bot):
    start,
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=start,
        resize_keyboard=True,
    )
    await message.answer (f'<b>Привет, {message.from_user.first_name}!</b> Я хочу помочь тебе! Что тебе нужно⁉📄', reply_markup=keyboard, parse_mode="HTML")

async def get_schedule_form(message: Message, state: FSMContext):
    await message.answer(f'<b>{message.from_user.first_name},</b> Выбери день недели🗓:',
                         reply_markup=keyboard_days_of_week)
    await state.set_state(StepsForm.GET_DAY)

async def get_day(message: Message, bot:Bot, state: FSMContext):
    await message.answer(f"<b>{message.from_user.first_name},</b> Введи <u>цифру и букву</u> класса📋: ", parse_mode="HTML")
    await state.update_data(day=message.text)
    await state.set_state(StepsForm.GET_NUM_AND_LETTER)

async def get_num_and_letter(message: Message, state: FSMContext):
    context_data = await state.get_data()
    await message.answer(f"Ты выбрал день недели🗓: \r\n{context_data.get('day')}\r\n"
                         f"Ты выбрал букву и номер класса📋: \r\n{message.text}\r\n",
                         reply_markup=keyboard_yes_no)
    await state.update_data(num_and_letter=message.text)
    await state.set_state(StepsForm.GET_SCHEDULE)

async def get_schedule_from_sparky(message: Message, state: FSMContext):

    context_data = await state.get_data()
    # await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
    day_of_week = str(context_data.get('day'))
    num_and_letter = str(context_data.get('num_and_letter'))
    print(day_of_week, num_and_letter)
    #Получаем расписание
    list_of_lessons, list_of_rooms = get_schedule(day_of_week, num_and_letter)
    print(list_of_lessons, list_of_rooms)

    lessons_string = ''
    for lesson, room in zip(list_of_lessons, list_of_rooms):
        lessons_string += str(lesson)
        lessons_string += " КАБ "
        lessons_string += str(room)
        lessons_string += '\n '
    print(lessons_string)

    # lessons_string = '\n'.join(map(str, list_of_lessons)) #Здесь мы используем метод джоин и мап для форматирования списка в удобную для отправки строку

    data_user = f'Вот твое расписание📇. \r\n' \
                f'Выбранный день недели🗓: {day_of_week}\r\n' \
                f'Выбранный класс📋: {num_and_letter}\r\n' \

    await message.answer(data_user)
    await message.answer(lessons_string)

    await state.clear()

async def get_no(message:Message, state: FSMContext):
    await state.clear()
    get_schedule_form()


