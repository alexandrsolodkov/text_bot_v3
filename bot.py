import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data import Config, load_config
from handlers import user_handlers

# from services.database.db_commands import UserCommand

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    config: Config = load_config('.env')
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)

    # db = UserCommand()
    try:
        await bot.send_message(chat_id=config.tg_bot.root, text='Бот запущен')
        # await db.create_user_table()
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
