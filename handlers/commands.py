from aiogram import  Dispatcher, types
import os
from config import bot



#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой telegram ID - {message.from_user.id}\n')

    await message.answer('Привет!')


#@dp.message_handler(commands=['cat'])
async def cat_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

#    photo = open(photo_path, 'rb')

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='Это котик')

        await message.answer_photo(photo=photo, caption='Котик')





def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(cat_handler, commands=['cat'])



