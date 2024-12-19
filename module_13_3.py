from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@router.message(Command("finish"))
async def cmd_finish(message: Message):
    await message.answer("Бот завершил свою работу.")
    await dp.stop_polling()

@router.message(F.text.lower() == "urban")
async def msg_urban(message: Message):
    await message.answer("Привет, Urban!")

@router.message()
async def msg_any(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Updates were skipped successfully.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    my_token = "Тут должен быть мой ТОКЕН"
    bot = Bot(token=my_token)
    dp = Dispatcher(storage=MemoryStorage())
    asyncio.run(main())