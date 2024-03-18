from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message
from aiogram.filters import Command
import logging
from core.handlers.basic import cmd_start_kb
from core.handlers.basic import get_schedule_form, get_schedule_from_sparky, get_day, get_num_and_letter, get_no
from core.settings import settings
import openpyxl
from core.utils.statestest import StepsForm
from aiogram.fsm.storage.memory import MemoryStorage
import emoji

book = openpyxl.load_workbook(filename='schedule.xlsx')


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="📳Бот ихвильнихтает📳")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="💤Бот устал💤")

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(cmd_start_kb, Command(commands=["start"]))
    dp.startup.register(start_bot)

    dp.shutdown.register(stop_bot)

    dp.message.register(get_schedule_form, F.text == "Расписание")
    dp.message.register(get_day, StepsForm.GET_DAY)
    dp.message.register(get_num_and_letter, StepsForm.GET_NUM_AND_LETTER)
    dp.message.register(get_schedule_from_sparky, StepsForm.GET_SCHEDULE)
    dp.message.register(get_no, F.text == "❌")



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())