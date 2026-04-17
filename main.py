import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
from threading import Thread

TOKEN = "8701135930:AAGBSojTbu3IG0JajC6HvovN2f4y8qv5jYc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.first_name
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # Hozircha Google'ni ulab turamiz, keyin o'z ilovangizni ulysiz
    web_app = WebAppInfo(url="https://www.google.com") 
    markup.add(KeyboardButton(text="Ilovani ochish 📱", web_app=web_app))
    
    await message.answer(f"✨ Assalomu alaykum {user_name}, KheroPin botiga xush kelibsiz 🤝", reply_markup=markup)

# Render uxlab qolmasligi uchun kichik server
app = Flask('')
@app.route('/')
def home(): return "Bot is running!"

def run(): app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    executor.start_polling(dp)
  
