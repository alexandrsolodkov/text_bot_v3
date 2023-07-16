from aiogram.filters.state import State, StatesGroup


class InputState(StatesGroup):
    take_vacancy = State()
    take_news = State()
