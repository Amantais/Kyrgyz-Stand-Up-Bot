
from aiogram import Dispatcher

from data.config import admins 

async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(admins, 'Bot is working')