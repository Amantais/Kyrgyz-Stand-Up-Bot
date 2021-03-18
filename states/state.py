from aiogram.dispatcher.filters.state import StatesGroup, State 

class StandUp(StatesGroup):
    have_problem = State()
    tomorrow_plan = State()
    bye = State()