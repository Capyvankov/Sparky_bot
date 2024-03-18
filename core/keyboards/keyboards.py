from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
import emoji

start = [
         [
            types.KeyboardButton(text="Расписание"),
            # types.KeyboardButton(text="ДЗ"),
         ],
    ]

kb_days_of_week = [
         [
            types.KeyboardButton(text="понедельник"),
            types.KeyboardButton(text="вторник"),
            types.KeyboardButton(text="среда"),

         ],
         [
            types.KeyboardButton(text="четверг"),
            types.KeyboardButton(text="пятница"),
            types.KeyboardButton(text="суббота"),
         ],
    ]

keyboard_days_of_week = ReplyKeyboardMarkup(
    keyboard=kb_days_of_week,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выбери день недели"
)

kb_yes_no = [
    [
            types.KeyboardButton(text="✅"),
            types.KeyboardButton(text="❌")
    ],
]
keyboard_yes_no = ReplyKeyboardMarkup(
    keyboard=kb_yes_no,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Всё верно?"
)