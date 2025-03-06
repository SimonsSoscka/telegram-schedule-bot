import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем токен из переменной окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Расписание (замени на своё)
SCHEDULE = """📅 Расписание на сегодня:
1️⃣ Пара 1 – 9:30-11:05
2️⃣ Пара 2 – 11:25-13:00
3️⃣ Пара 3 – 13:40-15:15
4️⃣ Пара 4 – 15:25-17:00
"""

# Обработчик команды /расписание
@dp.message_handler(commands=["расписание"])
async def send_schedule(message: types.Message):
    await message.reply(SCHEDULE)

# Запуск бота
if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
