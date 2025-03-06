import asyncio
import datetime
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.markdown import hbold

TOKEN = "7462721993:AAHaWBxQymZv19uBsSsS6ws9Cum13C1djrQ"  # Вставь сюда свой токен бота
CHAT_ID = 917911613  # Замени на свой Telegram ID (куда отправлять расписание)

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Функция для получения расписания (замени на свою логику)
def get_расписание():
    return (
        f"{hbold('📅 Расписание на сегодня:')}\n"
        "1️⃣ Пара 1 - 9:30\n"
        "2️⃣ Пара 2 - 11:25\n"
        "3️⃣ Пара 3 - 13:40\n"
        "4️⃣ Пара 4 - 15:25\n"
    )

# Команда /schedule для запроса расписания
@dp.message(Command("расписание"))
async def send_расписание(message: Message):
    расписание_text = get_schedule()
    await message.answer(расписание_text)

# Автоматическая отправка расписания в 8:00 утра
async def расписание_task():
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 0:  # Отправляет сообщение в 8:00
            расписание_text = get_расписание()
            await bot.send_message(CHAT_ID, расписание_text)
        await asyncio.sleep(60)  # Проверять время каждую минуту

async def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.create_task(расписание_task())  # Запускаем автоматическую отправку
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
