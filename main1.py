import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.fsm.storage.memory import MemoryStorage

api = "7558331550:AAEB_pws82bT41a1pNo3RVN-4XEiGBImV2s"
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)
