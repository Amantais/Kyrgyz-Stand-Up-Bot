from aiogram import types 
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext


from loader import dp
from keyboards.inline.callback_data import choice_callback
from keyboards.inline.choice_buttons import choice 
from states.state import StandUp
from stickers.su_stickers import soke 

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Салам <b>{message.from_user.first_name} 'Stand up'</b> отосунбу?",
                         reply_markup=choice)

@dp.callback_query_handler(choice_callback.filter(title='yes'))
async def standup_start(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer(f'Бугун эмне кылдын <b>{call.from_user.first_name}</b>?')
    await StandUp.have_problem.set()

@dp.message_handler(state=StandUp.have_problem)
async def tell_me_problem(message: types.Message, state: FSMContext):
    await message.answer('Бугун эмне проблемалар болду?')
    await StandUp.next()

@dp.message_handler(state=StandUp.tomorrow_plan)
async def write_tommorow(message: types.Message, state: FSMContext):
    await message.answer('Кандай пландар бар жакынкы арага?')
    await StandUp.next()


@dp.message_handler(state=StandUp.bye)
async def write_bye(message: types.Message, state: FSMContext):
    await message.answer('Чон рахмат Stand up отконуно 😄')
    await state.finish()


@dp.callback_query_handler(text='no')
async def standup_cancel(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_sticker(sticker=soke)