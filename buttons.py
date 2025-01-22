from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
    KeyboardButton('/cat'),
    KeyboardButton('/quiz'),
    KeyboardButton('/game'),
    KeyboardButton('/reply_webapp'),
    KeyboardButton('/inline_webapp'),
    KeyboardButton('/registration'))



submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(KeyboardButton('да'), KeyboardButton('нет'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                             one_time_keyboard=True).add(KeyboardButton('отмена'))

#size_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
#    KeyboardButton("S"), KeyboardButton("M"), KeyboardButton("L"),
#    KeyboardButton("XL"), KeyboardButton("2XL"), KeyboardButton("3XL"))



#удаление кнопки из интерфейса
remove_keyboard = ReplyKeyboardRemove()