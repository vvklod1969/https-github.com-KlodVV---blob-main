import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

api = "7558331550:AAEB_pws82bT41a1pNo3RVN-4XEiGBImV2s"
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я эхо бот.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
