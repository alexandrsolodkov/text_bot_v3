from aiogram import Router, F
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from config_data import load_config
# from filters import NewUser
from keyboards import create_nav_menu, create_to_user_menu
from lexicon import LEXICON
from services.input_states import InputState

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['welcome_text'].format(message.from_user.first_name))
    with open(file='services/activation_stat.txt', mode='a', encoding="utf-8") as pc:
        full_name = message.from_user.full_name
        user_name = message.from_user.username
        user_id = message.from_user.id
        usage_time = f'{message.date.year}-{message.date.month}-{message.date.day}'
        pc.write(f'{user_id}|{full_name}|{user_name}|{usage_time}' + '\n')


@router.message(~StateFilter(default_state), Command(commands='cancel'))
async def process_cancel_command_state(mesassge: Message, state: FSMContext):
    await state.clear()
    await mesassge.answer(text=LEXICON['menu'],
                          reply_markup=create_nav_menu(
                              'offer_news_btn', 'subscribe', 'buy_advertising_btn', 'sign_up_for_mentoring'))


@router.message(Command(commands='menu'), StateFilter(default_state))
async def process_menu_command(message: Message):
    await message.answer(text=LEXICON['menu'],
                         reply_markup=create_nav_menu(
                             'offer_news_btn', 'subscribe', 'buy_advertising_btn', 'sign_up_for_mentoring')
                         )


@router.callback_query(Text(text='to_menu'))
async def process_help_command(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['menu'],
                                     reply_markup=create_nav_menu(
                                         'offer_news_btn', 'subscribe', 'buy_advertising_btn', 'sign_up_for_mentoring')
                                     )


@router.callback_query(Text(text='buy_advertising_btn'))
async def process_advertising_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['buy_advertising'],
                                     reply_markup=create_nav_menu('to_menu'),
                                     disable_web_page_preview=True
                                     )


# @router.callback_query(Text(text='offer_vacancy_btn'))
# async def process_offer_vacancy_press(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(text=LEXICON['offer_vacancy'], disable_web_page_preview=True)
#     await state.set_state(InputState.take_vacancy)


# @router.message(StateFilter(InputState.take_vacancy),
#                 ~F.text.startswith('/'),
#                 F.content_type == ContentType.TEXT)
# async def process_vacancy_message_sent(message: Message, state: FSMContext):
#     username = message.from_user.username
#     user_url = message.from_user.url
#     await message.copy_to(chat_id=load_config().tg_bot.admin,
#                           reply_markup=create_to_user_menu(text=username, url=user_url)
#                           )
#     await message.answer(text=LEXICON['offer_vacancy_answer'],
#                          reply_markup=create_nav_menu('to_menu'))
#     await state.clear()


# @router.message(StateFilter(InputState.take_vacancy))
# async def warn_vacancy_message_sent(message: Message):
#     await message.answer(text=LEXICON['offer_vacancy_warning'])


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
    username = message.from_user.username
    user_url = message.from_user.url
    await message.copy_to(chat_id=load_config().tg_bot.admin,
                          reply_markup=create_to_user_menu(text=username, url=user_url)
                          )
    await message.answer(text=LEXICON['offer_news_answer'],
                         reply_markup=create_nav_menu('to_menu'))
    await state.clear()


@router.message(StateFilter(InputState.take_news))
async def warn_news_message_sent(message: Message):
    await message.answer(text=LEXICON['offer_news_warning'])


# @router.callback_query(Text(text='additional_services_btn'))
# async def process_mentor_press(callback: CallbackQuery):
#     await callback.message.edit_text(text=LEXICON['additional_services'],
#                                      reply_markup=create_nav_menu('to_menu'),
#                                      disable_web_page_preview=True
#                                      )

@router.callback_query(Text(text='subscribe'))
async def process_subscribe_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['subscribe_btn'],
                                     reply_markup=create_nav_menu('to_menu'),
                                     disable_web_page_preview=True
                                     )


@router.callback_query(Text(text='sign_up_for_mentoring'))
async def process_subscribe_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['sign_up_for_mentoring_btn'],
                                     reply_markup=create_nav_menu('to_menu'),
                                     disable_web_page_preview=True
                                     )
