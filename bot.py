from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive"

if __name__ == '__main__':
    import threading
    threading.Thread(target=app.run).start()
    app.run(host='0.0.0.0', port=10000)  # Указываем порт здесь
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardButton
)
import asyncio

# Настройки бота
API_TOKEN = "7692869160:AAEZmtbmovXVZu590Ll4mmZbIbsM6xPdjUI"
REF_LINK = "https://bit.ly/edacourier5"  # Ваша реферальная ссылка

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ---- Клавиатуры ----
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✨ Подробнее")]
    ],
    resize_keyboard=True
)

courier_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="🚀 Стать курьером",
            url=REF_LINK
        )]
    ]
)


# ---- Обработчики ----
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "<b>👋 Добро пожаловать в бот для курьеров Яндекс Еды!</b>\n\n"
        "Здесь ты можешь узнать условия работы и подать заявку.\n\n"
        "Нажми <b>«Подробнее»</b>, чтобы продолжить! 💫",
        reply_markup=start_keyboard,
        parse_mode="HTML"
    )


@dp.message(lambda message: message.text == "✨ Подробнее")
async def show_details(message: types.Message):
    text = (
        "<b>🔥Ваши выгоды:</b>\n\n"
        "✅<b>До 9000₽ в день + 100% чаевых</b> (выплаты ежедневно)\n"
        "✅<b>Свободный график</b> - выбирайте комфортное время для работы\n"
        "✅<b>Работа в своём районе</b> - никаких дальних маршрутов\n"
        "✅<b>Бонусы для курьеров</b> - система рейтинга, цели, скидки\n"
        "✅<b>Выбирайте способ доставки</b> (пеший, вело, авто)\n"
        "✅<b>Легкие заказы</b> - из ресторанов, магазинов и аптек\n\n"
        "📌Как начать?\n"
        "1️⃣Нажать кнопку <b>«🚀 Стать курьером»</b>\n"
        "2️⃣Пройти обучение (5-10 минут)\n"
        "3️⃣Забрать сумку и начать зарабатывать!\n\n"
        "👇<b>Успейте! Свободных мест осталось: 5.</b>"
    )

    await message.answer(
        text,
        reply_markup=courier_keyboard,
        parse_mode="HTML"
    )


# ---- Запуск ----
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())