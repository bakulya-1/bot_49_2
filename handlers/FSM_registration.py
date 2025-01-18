from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from babel.plural import within_range_list

import buttons
from db import main_db


class FSM_reg(StatesGroup):
    fullname = State()
    age = State()
    email = State()
    city = State()
    photo = State()
    submit = State()


async  def start_fsm_reg(message: types.Message):
    await FSM_reg.fullname.set()
    await message.answer('Напишите фио:')


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await FSM_reg.next()
    await message.answer('Напишите свой возраст')

async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await FSM_reg.next()
    await message.answer('Отправьте свою почту')

async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await FSM_reg.next()
    await message.answer('В каком городе вы проживаете')

async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await FSM_reg.next()
    await message.answer('Отправьте свою фотографию')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await FSM_reg.next()
        await message.answer('Верные ли данные ?')
        await message.answer_photo(photo=data['photo'],
                                   caption=f'ФИО - {data["fullname"]}\n'
                                    f'Возраст - {data["age"]}\n'
                                    f'Почта - {data["email"]}\n'
                                    f'Город - {data["city"]}\n', reply_markup=buttons.submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':

        async with state.proxy() as data:
            await main_db.sql_insert_registered(
                fullname=data['fullname'],
                age=data['age'],
                email=data['email'],
                city=data['city'],
                photo=data['photo']
            )

            await message.answer('Ваши данные в базе', reply_markup=buttons.remove_keyboard)

        await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')



async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard)


def register_handlers_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(start_fsm_reg, commands='registration')
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_age, state=FSM_reg.age)
    dp.register_message_handler(load_email, state=FSM_reg.email)
    dp.register_message_handler(load_city, state=FSM_reg.city)
    dp.register_message_handler(load_photo, state=FSM_reg.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_reg.submit)




class FSM_store(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo1 = State()
    submit1 = State()
    productid = State()
    infoproduct = State()


async def start_fsm_store(message: types.Message):
    await FSM_store.name.set()
    await message.answer('Напишите название товара')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await FSM_store.next()
    await message.answer('Выберите размер товара: S, M, L, XL, 2XL, 3XL')

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_store.next()
    await  message.answer('Выберите категорию товара: одежда, обувь')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSM_store.next()
    await message.answer('Напишите стоимоть товара')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSM_store.next()
    await  message.answer('Отправьте фотографию товара')

async def load_photo1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo1'] = message.photo[-1].file_id

    await FSM_store.next()
    await message.answer('Подтвердите данные')
    await message.answer_photo(photo=data['photo1'],
                               caption=f'Товар - {data["name"]}\n'
                                       f'Размер - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Стоимость - {data["price"]}\n', reply_markup=buttons.submit)

async def submit1(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            productid = await main_db.store(
                name=data['name'],
                size = data['size'],
                price = data['price'],
                photo = data['photo1'],
                category = data['category']
            )
            await main_db.sql_insert_products_details(
                productid,
                data['category'],
                data.get('infoproduct', 'Нет информации')
            )


            await message.answer(f'Товар добавлен в базу', reply_markup=buttons.remove_keyboard)

            await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Хоршо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()
    else:
        await message.answer('Выберите да или нет')

async def cancel_fsm1(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard())

def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(start_fsm_store, commands='registration', state=None)
    dp.register_message_handler(load_name, state=FSM_store.name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo1, state=FSM_store.photo1, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_store.submit1)






