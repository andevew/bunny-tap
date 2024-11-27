from aiogram import Bot, Dispatcher, F
from aiogram.types import WebAppInfo, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
import asyncio

# Введи свій токен бота
BOT_TOKEN = "8050124746:AAF5ZfJfubCrsPRUhr8kSV4QyyI0uax64EE"

# Введи URL свого Telegram Web App
WEB_APP_URL = "https://test-task-seven-taupe.vercel.app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

# Клавіатура з кнопкою Web App
web_app = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Відкрити Web App", web_app=WebAppInfo(url=WEB_APP_URL))
    ]]
)

@dp.message(CommandStart())
async def send_web_app(message: Message):
    await message.answer(
        "Привіт! Натисни кнопку нижче, щоб відкрити наш веб-додаток:",
        reply_markup=web_app
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
