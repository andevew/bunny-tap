from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

web_app = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='"Відкрити Web App"', callback_data='web-app')]]
)