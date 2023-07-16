from aiogram import Router, F
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery, ContentType

from config_data import load_config
from keayboards import create_nav_menu
from lexicon import LEXICON
from services.input_states import InputState

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['welcome_text'].format(message.from_user.first_name))


@router.message(~StateFilter(default_state), Command(commands='cancel'))
async def process_cancel_command_state(mesassge: Message, state: FSMContext):
    await state.clear()
    await mesassge.answer(text=LEXICON['menu'],
                          reply_markup=create_nav_menu(
                              'buy_advertising_btn', 'offer_vacancy_btn', 'offer_news_btn', 'mentor_btn'))


@router.message(Command(commands='menu'), StateFilter(default_state))
async def process_menu_command(message: Message):
    await message.answer(text=LEXICON['menu'],
                         reply_markup=create_nav_menu(
                             'buy_advertising_btn', 'offer_vacancy_btn', 'offer_news_btn', 'mentor_btn')
                         )


@router.callback_query(Text(text='to_menu'))
async def process_help_command(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['menu'],
                                     reply_markup=create_nav_menu(
                                         'buy_advertising_btn', 'offer_vacancy_btn', 'offer_news_btn', 'mentor_btn')
                                     )


@router.callback_query(Text(text='buy_advertising_btn'))
async def process_advertising_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['buy_advertising'],
                                     reply_markup=create_nav_menu('to_menu'),
                                     disable_web_page_preview=True
                                     )


@router.callback_query(Text(text='offer_vacancy_btn'))
async def process_offer_vacancy_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=LEXICON['offer_vacancy'], disable_web_page_preview=True)
    await state.set_state(InputState.take_vacancy)


@router.message(StateFilter(InputState.take_vacancy),
                ~F.text.startswith('/'),
                F.content_type == ContentType.TEXT)
async def process_vacancy_message_sent(message: Message, state: FSMContext):
    await message.send_copy(chat_id=load_config().tg_bot.root)
    await message.answer(text=LEXICON['offer_vacancy_answer'],
                         reply_markup=create_nav_menu('to_menu'))
    await state.clear()


@router.message(StateFilter(InputState.take_vacancy))
async def warn_vacancy_message_sent(message: Message):
    await message.answer(text=LEXICON['offer_vacancy_warning'])


@router.message(StateFilter(default_state))
async def send_echo(message: Message):
    await message.reply(text=LEXICON['no_command_text'])


@router.callback_query(Text(text='offer_news_btn'))
async def process_news_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(LEXICON['offer_news'])
    await state.set_state(InputState.take_news)


@router.message(StateFilter(InputState.take_news),
                ~F.text.startswith('/'),
                F.content_type.in_({'photo', 'video', 'text'}))
async def process_news_message_sent(message: Message, state: FSMContext):
    await message.send_copy(chat_id=load_config().tg_bot.root)
    await message.answer(text=LEXICON['offer_news_answer'],
                         reply_markup=create_nav_menu('to_menu'))
    await state.clear()


@router.message(StateFilter(InputState.take_news))
async def warn_news_message_sent(message: Message):
    await message.answer(text=LEXICON['offer_news_warning'])


@router.callback_query(Text(text='mentor_btn'))
async def process_mentor_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['mentor'],
                                     reply_markup=create_nav_menu('to_menu'))
