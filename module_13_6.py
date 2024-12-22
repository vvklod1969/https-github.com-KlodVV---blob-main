from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# Добавили необходимые импорты для работы с inline-клавиатурами.
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import asyncio

router = Router()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создаем обычную клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Информация")],
        [KeyboardButton(text="Рассчитать")],
    ],
    resize_keyboard=True
)

# Создаем Inline-клавиатуру
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
            InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
        ]
    ]
)

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Отправляет приветственное сообщение и обычную клавиатуру
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=keyboard)


# Обработчик для кнопки "Рассчитать" - отправляет Inline-меню
@router.message(F.text.lower() == "рассчитать")
async def main_menu(message: Message):
    # Отправляет сообщение с inline клавиатурой
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

# Обработчик callback-запроса для "Формулы расчёта"
@router.callback_query(F.data == "formulas")
async def get_formulas(call: CallbackQuery):
    # Отправляет сообщение с формулой Миффлина-Сан Жеора
    formula_text = "Формула Миффлина-Сан Жеора (для женщин):\n10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161"
    await call.message.answer(formula_text)
    await call.answer() # Необходимо для завершения обработки callback'a

# Обработчик callback-запроса для "Рассчитать норму калорий"
@router.callback_query(F.data == "calories")
async def set_age(call: CallbackQuery, state: FSMContext):
    # Запускает машину состояний
    await call.message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)
    await call.answer() # Необходимо для завершения обработки callback'a

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

@router.message(F.text.lower() == "информация")
async def msg_info(message: Message):
    await message.answer("Программа для расчета калорий!")

@router.message(F.text.lower() == "спасибо")
async def msg_thanks(message: Message):
    await message.answer("Всегда пожалуйста, обращайтесь!")

async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Updates were skipped successfully.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    my_token = "Мой ТОКЕН"
    bot = Bot(token=my_token)
    dp = Dispatcher(storage=MemoryStorage())
    asyncio.run(main())