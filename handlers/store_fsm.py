
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import  Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import  FSMContext
from db import main_db
import buttons




class StoreFSM(StatesGroup):
    name_product = State()
    size = State()
    price = State()
    category = State()
    info_product = State()
    products_id = State()
    photo = State()
    collection = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await StoreFSM.name_product.set()
    await message.answer('Напишите название товара:', reply_markup=buttons.cancel)

async def name_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите размер: ')

async def size_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size_product'] = message.text

    await StoreFSM.next()
    await  message.answer('Введите цену товара: ')

async def price_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите категорию товара: ')

async def category_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category_product'] = message.text

    await StoreFSM.next()
    await  message.answer('Введите информацию о продукте: ')

async def info_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите артикул для товара: ')

async def product_id_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['products_id'] = message.text

    await StoreFSM.next()
    await message.answer('Отправьте фото товара: ')

async def photo_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

async def collection_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

    await StoreFSM.next()
    await message.answer('Подтвердите данные.', reply_markup=buttons.submit)

    await message.answer_photo(photo=data['photo'],
                               caption=f'Название товара - {data["name_product"]}\n'
                                       f'Размер товара- {data["size_product"]}\n'
                                       f'Категория - {data["category_product"]}\n'
                                       f'Артикул - {data["products_id"]}\n'
                                       f'Инфо - {data["info_product"]}\n'
                                       f'Стоимость - {data["price_product"]}\n'
                                       f'Коллекция - {data["collection"]}\n')

async def submit_load(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name_product=data['name_product'],
                size = data['size_product'],
                price = data['price_product'],
                product_id = data['products_id'],
                photo = data['photo']
            )
            await main_db.sql_insert_detail(
                product_id=data['products_id'],
                info_product=data['info_product'],
                category=data['category_product']
            )
            await main_db.sql_insert_collection(
                collection=data['collection'],
                product_id=data['prodict_id']
            )

            await message.answer(f'Ваши данные в базе!', reply_markup=buttons.remove_keyboard)
            await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


"""""
async def cancel_fsm1(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard())
"""""


def register_handlers_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['store'])

    dp.register_message_handler(name_load, state=StoreFSM.name_product)
    dp.register_message_handler(size_load, state=StoreFSM.size)
    dp.register_message_handler(price_load, state=StoreFSM.price)
    dp.register_message_handler(category_load, state=StoreFSM.category)
    dp.register_message_handler(info_load, state=StoreFSM.info_product)
    dp.register_message_handler(product_id_load, state=StoreFSM.products_id)
    dp.register_message_handler(photo_load, state=StoreFSM.photo, content_types=['photo'])
    dp.register_message_handler(collection_load, state=StoreFSM.collection)
    dp.register_message_handler(submit_load, state=StoreFSM.submit)




