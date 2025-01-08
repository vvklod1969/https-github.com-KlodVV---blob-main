from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
# from products import products # Удаляем импорт словаря продуктов
import asyncio
from crud_functions import initiate_db, get_all_products # Импортируем функции для работы с бд

router = Router()

class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()
    activity = State()

# Создаем обычную клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Информация")],
        [KeyboardButton(text="Рассчитать")],
        [KeyboardButton(text="Купить")],
    ],
    resize_keyboard=True
)

# Создаем Inline-клавиатуру для главного меню
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
            InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
        ]
    ]
)

# inline-клавиатура выбора пола
gender_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мужчина", callback_data="male"),
         InlineKeyboardButton(text="Женщина", callback_data="female")]
    ]
)

# inline-клавиатура выбора коэффициента активности
activity_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Сидячий образ жизни", callback_data="1.2")],
        [InlineKeyboardButton(text="Низкая активность (1-3 раза в неделю)", callback_data="1.375")],
        [InlineKeyboardButton(text="Средняя активность (3-5 раз в неделю)", callback_data="1.55")],
        [InlineKeyboardButton(text="Высокая активность (6-7 раз в неделю)", callback_data="1.725")],
        [InlineKeyboardButton(text="Очень высокая активность (2 раза в день)", callback_data="1.9")],
    ]
)

# Создаем Inline-клавиатуру для списка продуктов
products_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
    ]
)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=keyboard)


@router.message(F.text.lower() == "рассчитать")
async def main_menu(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
         await message.answer("Вы уже запустили расчет. Пожалуйста, завершите его.")
    else:
        await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@router.callback_query(F.data == "formulas")
async def get_formulas(call: CallbackQuery):
    formula_text = "Формула Миффлина-Сан Жеора:\nДля женщин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161\nДля мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.answer(formula_text)
    await call.answer()

@router.callback_query(F.data == "calories")
async def set_gender(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите свой пол:", reply_markup=gender_keyboard)
    await state.set_state(UserState.gender)
    await call.answer()

@router.callback_query(UserState.gender, F.data.in_(["male", "female"]))
async def set_age(call: CallbackQuery, state: FSMContext):
    await state.update_data(gender=call.data)
    await call.message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)
    await call.answer()

@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            await message.answer("Пожалуйста, введите корректный возраст.")
            return
        await state.update_data(age=age)
        await message.answer("Введите свой рост (см):")
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer("Пожалуйста, введите возраст цифрами.")

@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth <= 0:
            await message.answer("Пожалуйста, введите корректный рост.")
            return
        await state.update_data(growth=growth)
        await message.answer("Введите свой вес (кг):")
        await state.set_state(UserState.weight)
    except ValueError:
         await message.answer("Пожалуйста, введите рост цифрами.")

@router.message(UserState.weight)
async def set_activity(message: Message, state: FSMContext):
    try:
        weight = int(message.text)
        if weight <= 0:
            await message.answer("Пожалуйста, введите корректный вес.")
            return
        await state.update_data(weight=weight)
        await message.answer("Выберите свой коэффициент активности:", reply_markup=activity_keyboard)
        await state.set_state(UserState.activity)
    except ValueError:
        await message.answer("Пожалуйста, введите вес цифрами.")

@router.callback_query(UserState.activity, F.data.in_(["1.2", "1.375", "1.55", "1.725", "1.9"]))
async def send_calories(call: CallbackQuery, state: FSMContext):
    await state.update_data(activity=float(call.data))
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    gender = data['gender']
    activity = float(data['activity'])
    if gender == "male":
        calories = (10 * weight + 6.25 * growth - 5 * age + 5) * activity
    else:
        calories = (10 * weight + 6.25 * growth - 5 * age - 161) * activity
    await call.message.answer(f"Ваша норма калорий: {calories:.2f}")
    await call.message.answer("Расчёт завершён. ", reply_markup=keyboard)
    await state.set_state(None)
    await call.answer()

@router.message(F.text.lower() == "информация")
async def msg_info(message: Message):
    await message.answer("Программа для расчета калорий!")

@router.message(F.text.lower() == "спасибо")
async def msg_thanks(message: Message):
    await message.answer("Всегда пожалуйста, обращайтесь!")

@router.message(F.text.lower() == "купить")
async def get_buying_list(message: Message):
    products = get_all_products()
    for product in products:
        await message.answer_photo(
            photo=product[4],  # Используем URL-адрес изображения из базы данных
            caption=f"Название: {product[1]}\nОписание: {product[2]}\nЦена: {product[3]}"
        )
    #обновляем клавиатуру
    products = get_all_products()
    products_keyboard.inline_keyboard = [[InlineKeyboardButton(text=product[1], callback_data="product_buying")]
        for product in products]

    await message.answer("Выберите продукт для покупки:", reply_markup=products_keyboard)

@router.callback_query(F.data == "product_buying")
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer() # Необходимо для завершения обработки callback'a

async def main():
    initiate_db()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Updates were skipped successfully.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    my_token = "7558331550:AAEB_pws82bT41a1pNo3RVN-4XEiGBImV2s"
    bot = Bot(token=my_token)
    dp = Dispatcher(storage=MemoryStorage())
    asyncio.run(main())