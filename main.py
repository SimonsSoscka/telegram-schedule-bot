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

if name == "__main__":
    asyncio.run(main())
