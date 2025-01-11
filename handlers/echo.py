from aiogram import Dispatcher, types
import re


#async  def echo_handler(message: types.Message):
#    await message.answer(message.text)
#@dp.message_handler()
async  def echo_handler(message: types.Message):
    text = message.text

    if re.match(r'^-?\d+(\.\d+)?$', text):
        number = float(text)
        squared = number ** 2
        await message.answer(f'Число в квадрате {squared}')
    else:
        await message.answer(text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
