from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyexpat.errors import messages

from config import bot
import os
import random


async def  quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    button = InlineKeyboardButton('Далее', callback_data='button1')

    keyboard.add(button)

    question = 'BMW or Mercedes'

    answer  = ['BMW', 'Mercedes', 'Оба']

    await bot.send_poll(
        chat_id=message.chat.id,     # Куда отправить
        question=question,           # Сам вопрос
        options=answer,              # Ответы
        is_anonymous=False,          # Анонимный или нет
        type='quiz',                 # Тип опросника
        correct_option_id=0,         # Правильный ответ
        explanation='Не-а',          # Подсказка
        open_period=60,              # Время работы опросника
        reply_markup=keyboard        # Добавление кнопки
    )

async  def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    button = InlineKeyboardButton('Далее', callback_data='button2')

    keyboard.add(button)

    question = 'Dota2 or CS GO'
    answer = ['Dota2', 'CS GO']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Эх ты...',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    button = InlineKeyboardButton('Далее', callback_data='button3')

    keyboard.add(button)

    question = 'Ужасы or Фильмы'
    answer = ['Ужасы', 'Фильмы']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Хе-хе',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_4(call: types.CallbackQuery):

    question = 'Apple or Android'
    answer = ['Apple', 'Android', 'Оба']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Вот так',
        open_period=60
    )
    photo_path = os.path.join('media', 'img_1.png')
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=question,
        )




games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

game_state = {}

async def game_dice(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Выберите игру: \n\n1. ⚽ Футбол\n2. 🎰 Слот-машина\n3. 🏀 Баскетбол\n4. 🎯 Мишень\n5. 🎳 Боулинг\n6. 🎲 Кости\n",
    )

    game_state[message.chat.id] = {"status": "waiting_for_game_choice"}

async def game_choice(message: types.Message):
    chat_id = message.chat.id
    if chat_id not in game_state or game_state[chat_id]["status"] != "waiting_for_game_choice":
        return

    choice = message.text.strip()

    if choice == "1" or choice.lower() == "футбол":
        await  start_football_game(message)
    elif choice == "2" or choice.lower() == "слот-машина":
        await start_slot_machine(message)
    elif choice == "3" or choice.lower() == "баскетбол":
        await start_basketball_game(message)
    elif choice == "4" or choice.lower() == "мишень":
        await  start_dart_game(message)
    elif choice == "5" or choice.lower() == "боулинг":
        await start_bowling_game(message)
    elif choice == "6" or choice.lower() == "кости":
        await  start_dice_game(message)
    else:
        await  bot.send_message(chat_id, "Попробуйте снова.")
        return

async def start_football_game(message: types.Message):
    player_score = random.randint(0, 5)
    bot_score = random.randint(0,5)

    result = "Вы забили гол!" if player_score > bot_score else "Бот забил гол!"
    game_state[message.chat.id] = {"status": "game_in_progress", "game": "football"}

    await bot.send_message(chat_id=message.chat.id, text=f"Футбол:\nВаш результат: {player_score},\nРезультат бота: {bot_score}. {result}")


async def start_slot_machine(message: types.Message):
    player_symbols = [random.choice(["✈", "💲", "☠", "🍀"]) for _ in range(3)]
    bot_symbols = [random.choice(["✈", "💲", "☠", "🍀"]) for _ in range(3)]

    if player_symbols == bot_symbols:
        result = "Вы выиграли! Поздравляю!"
    else:
        result = "Не повезло, попробуйте снова."

    game_state[message.chat.id] = {"status": "game_in_progress", "game": "slot_machine"}

    await bot.send_message(chat_id=message.chat.id, text=f"Слот-машина:\nИгрок: {''.join(player_symbols)}\nБот: {''.join(bot_symbols)}\n{result}")


async def start_basketball_game(message: types.Message):
    player_shoot = random.randint(1, 5)
    bot_shoot = random.randint(1, 5)

    result = "Вы попали в корзину!" if player_shoot > 5 else "Вы промахнулись!"
    bot_result = "Бот попал в корзину!" if bot_shoot > 5 else "Бот промахнулся!"

    game_state[message.chat.id] = {"status": "game_in_progress", "game": "basketball"}

    await bot.send_message(chat_id=message.chat.id, text=f"Баскетбол:\nВаш бросок: {player_shoot} (результат: {result})\nБот: {bot_shoot} (результат: {bot_result})")


async def start_dart_game(message: types.Message):
    player_score = random.randint(0, 50)
    bot_score = random.randint(0, 50)

    result = "Вы выиграли!" if player_score > bot_score else "Бот выиграл!"

    game_state[message.chat.id] = {"status": "game_in_progress", "game": "dart"}

    await bot.send_message(chat_id=message.chat.id, text=f"Мишень (Дартс):\nВаш результат: {player_score}\nРезультат бота: {bot_score}\n{result}")


async def start_bowling_game(message: types.Message):
    player_pins = sum(random.randint(0, 10) for _ in range (5))
    bot_pins = sum(random.randint(0, 10) for _ in range(5))

    result = "Вы победили!" if player_pins > bot_pins else "Бот победил!"

    game_state[message.chat.id] = {"status": "game_in_progress", "game": "bowling"}

    await bot.send_message(chat_id=message.chat.id, text=f"Боулинг:\nВаш результат: {player_pins} сбитых кеглей\nРезультат бота: {bot_pins} сбитых кеглей\n {result}")


async def start_dice_game(message: types.Message):
    player_roll = random.randint(1, 6)
    bot_roll = random.randint(1,6)

    result = "Вы победили!" if player_roll > bot_roll else "Бот победил!"

    game_state[message.chat.id] = {"status": "game_in_progress", "game": "dice"}

    await bot.send_message(chat_id=message.chat.id, text=f"Кости:\nВаш бросок: {player_roll}\nБот: {bot_roll}\n{result}")




game_state = {}

dice_symbols = ['⚽', '🎰', '🏀']
dice_descriptions = {
    '⚽': "Футбол. Бот и игрок пытаются забить гол.",
    '🎰': "Слот-машина. Играем на удачу!",
    '🏀': "Баскетбол. Кто попадет в корзину?"
}


async def start_game(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Выберите один из 3 дайсов:\n1. ⚽ Футбол\n2. 🎰 Слот-машина\n3. 🏀 Баскетбол\n"
             "Введите 1, 2 или 3, чтобы выбрать."
    )
    game_state[message.chat.id] = {"status": "waiting_for_dice_choice"}


async def game_choice(message: types.Message):
    chat_id = message.chat.id

    if game_state.get(chat_id, {}).get("status") == "waiting_for_dice_choice":
        choice = message.text.strip()

        if choice == "1" or choice.lower() == "⚽":
            await start_dice_game(message, '⚽')
        elif choice == "2" or choice.lower() == "🎰":
            await start_dice_game(message, '🎰')
        elif choice == "3" or choice.lower() == "🏀":
            await start_dice_game(message, '🏀')
        else:
            await bot.send_message(chat_id, "Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
            return

        game_state[chat_id]["status"] = "game_in_progress"
#    else:
#        await bot.send_message(chat_id, "Сначала начните новую игру командой /game.")


async def start_dice_game(message: types.Message, dice: str):
    chat_id = message.chat.id


    player_roll = random.randint(1, 6)
    bot_roll = random.randint(1, 6)

    await bot.send_message(chat_id, f"Вы выбрали {dice}. Результаты игры:")

    if dice == '⚽':
        result = await play_football(player_roll, bot_roll)
    elif dice == '🎰':
        result = await play_slot_machine(player_roll, bot_roll)
    elif dice == '🏀':
        result = await play_basketball(player_roll, bot_roll)


    await bot.send_message(chat_id, result)

    game_state[chat_id]["status"] = "game_finished"


# ⚽
async def play_football(player_roll, bot_roll):
    if player_roll > bot_roll:
        return f"Ваш бросок: {player_roll}. Бот бросил: {bot_roll}. Вы забили гол и выиграли!"
    elif bot_roll > player_roll:
        return f"Ваш бросок: {player_roll}. Бот бросил: {bot_roll}. Бот забил гол и выиграл!"
    else:
        return f"Ваш бросок: {player_roll}. Бот бросил: {bot_roll}. Ничья!"

# 🎰
async def play_slot_machine(player_roll, bot_roll):

    player_symbols = ["🍒", "🍇", "🍀", "🍉", "🍓"]
    bot_symbols = ["🍒", "🍇", "🍀", "🍉", "🍓"]

    player_spin = random.choice(player_symbols)
    bot_spin = random.choice(bot_symbols)

    if player_spin == bot_spin:
        return f"Вы оба вытащили {player_spin}. Это ничья!"
    elif player_spin != bot_spin:
        return f"Вы вытащили {player_spin}, а Бот {bot_spin}. Победил {player_spin}!"

#🏀
async def play_basketball(player_roll, bot_roll):
    if player_roll > bot_roll:
        return f"Ваш бросок: {player_roll}. Бот бросил: {bot_roll}. Вы забили в корзину и выиграли!"
    elif bot_roll > player_roll:
        return f"Ваш бросок: {player_roll}. Бот бросил: {bot_roll}. Бот забил в корзину и выиграл!"
    else:
        return f"Ваш бросок: {player_roll}. Бот бросил: {bot_roll}. Ничья!"



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button1')
    dp.register_callback_query_handler(quiz_3, text='button2')
    dp.register_callback_query_handler(quiz_4, text='button3')


#def register_handlers(dp: Dispatcher):
    dp.register_message_handler(game_dice, commands=['game'])
    dp.register_message_handler(game_choice)

    dp.register_message_handler(start_game, commands=['game'])
    dp.register_message_handler(game_choice)





