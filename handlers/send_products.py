from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import main_db



async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)

    buttons_all = types.InlineKeyboardButton('Ввывести все товары', callback_data='send_all_products')
    buttons_one = types.InlineKeyboardButton('Ввывести по одному', callback_data='send_one_products')

    keyboard.add(buttons_all, buttons_one)

    await message.answer('Выберите как просмотреть товары:' , reply_markup=keyboard)


async def send_all_products(call: types.CallbackQuery):
    products = main_db.fetch_all_products()

    if products:
        for product in products:
            caption = (f'Название товара - {product["name_product"]}\n'
                       f'Размер товара  - {product["size"]}\n'
                       f'Категория - {product["category"]}\n'
                       f'Артикул - {product["products_id"]}\n'
                       f'Инфо - {product["info_product"]}\n'
                       f'Цена - {product["price"]}')


            await call.message.answer_photo(photo=product["photo"], caption=caption)


    else:
        await call.message.answer('База пуста! Товаров нет.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=['send_store'])
    dp.register_callback_query_handler(send_all_products, Text(equals='send_all_products'))

