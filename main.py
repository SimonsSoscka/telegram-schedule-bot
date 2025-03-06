from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher

TOKEN = "7462721993:AAHaWBxQymZv19uBsSsS6ws9Cum13C1djrQ"

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    await bot.send_message(chat_id="917911613", text="Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    import logging
import os
from aiogram import Bot, Dispatcher

# Включаем логирование, чтобы видеть ошибки
logging.basicConfig(level=logging.INFO)

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен есть (чтобы избежать ошибки)
if not TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")

# Создаём объект бота
bot = Bot(token=TOKEN)

# Создаём диспетчер (обработчик команд и сообщений)
dp = Dispatcher(bot)
# Обрабатываем команду /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот для расписания.")

# Обрабатываем команду /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Я могу присылать расписание занятий!")

# Обрабатываем любые текстовые сообщения
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")
    if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
