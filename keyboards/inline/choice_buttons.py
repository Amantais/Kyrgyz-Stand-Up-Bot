from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import choice_callback

choice = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)

yes_buttons = InlineKeyboardButton(text='Ооба', callback_data='choice:yes')
no_buttons = InlineKeyboardButton(text='Жок', callback_data='no')
choice.insert(yes_buttons)
choice.insert(no_buttons)