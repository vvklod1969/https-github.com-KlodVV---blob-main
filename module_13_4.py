from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import asyncio

router = Router()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@router.message(F.text.lower() == "urban")
async def msg_urban(message: Message):
    await message.answer("Привет, Urban!")

@router.message(F.text.lower() == "calories")
async def cmd_calories(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)

@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)

@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)

@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    # упрощенная формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.set_state(None)

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