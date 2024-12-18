# Домашнее задание по теме "Хендлеры обработки сообщений".
# Задача "Бот поддержки (Начало)"

from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    print("Привет! Я бот помогающий твоему здоровью.")


@router.message(Command("finish"))
async def cmd_finish(message: Message):
    print("Бот завершил свою работу.")
    await dp.stop_polling()


@router.message(F.text.lower() == "urban")
async def msg_urban(message: Message):
    print("Привет, Urban!")


@router.message()
async def msg_any(message: Message):
    print("Введите команду /start, чтобы начать общение.")


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Updates were skipped successfully.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    my_token = "Тут должен быть мой ТОКЕН"  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    bot = Bot(token=my_token)
    dp = Dispatcher(storage=MemoryStorage())
    asyncio.run(main())