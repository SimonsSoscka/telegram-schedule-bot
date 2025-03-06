import asyncio
import datetime
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties

TOKEN = "7462721993:AAHaWBxQymZv19uBsSsS6ws9Cum13C1djrQ"  # Замени на свой токен
CHAT_ID = 917911613  # Твой Telegram ID

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Функция для получения расписания (замени на свою логику)
def get_schedule():
    return (
        f"{hbold('📅 Расписание на сегодня:')}\n"
        "1️⃣ Пара 1 - 9:30\n"
        "2️⃣ Пара 2 - 11:25\n"
        "3️⃣ Пара 3 - 13:40\n"
        "4️⃣ Пара 4 - 15:25\n"
    )

# Команда /schedule для запроса расписания
@dp.message(Command("schedule"))
async def send_schedule(message: Message):
    schedule_text = get_schedule()
    await message.answer(schedule_text)

# Автоматическая отправка расписания в 8:00 утра
async def scheduled_task():
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 0:
            schedule_text = get_schedule()
            await bot.send_message(CHAT_ID, schedule_text)
            await asyncio.sleep(60)  # Ждать минуту перед следующей проверкой
        await asyncio.sleep(1)  # Проверять время каждую секунду

async def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.create_task(scheduled_task())  # Запуск фоновой задачи
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
