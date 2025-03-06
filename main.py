import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен бота (замени на свой)
TOKEN = "7462721993:AAHaWBxQymZv19uBsSsS6ws9Cum13C1djrQ"

# Создаём экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обрабатываем команду /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой Сын.")

# Обрабатываем команду /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Я могу присылать расписание занятий!")

# Обрабатываем любые текстовые сообщения (эхо)
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

# Главная функция запуска бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
