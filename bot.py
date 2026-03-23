import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = 'YOUR_TOKEN_HERE'
WEBAPP_URL = 'https://3000-im366ggkc2bkg9sys37ec.app.cto.new'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text="🛍️ Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL)))
    await message.answer("👋 Добро пожаловать!", reply_markup=markup)

if __name__ == "__main__":
    print("✅ Бот запущен!")
    executor.start_polling(dp, skip_updates=True)
