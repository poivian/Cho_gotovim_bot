import asyncio
from os import getenv
from logging import getLogger

from aiogram import Dispatcher, Bot
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv

from handlers.user import user

from logger import init_logger

load_dotenv()
init_logger()
log = getLogger(__name__)

async def main():
    log.info('run...')
    bot = Bot(token=getenv('API_KEY_TELEGRAM'),
              default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_routers(user)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main(),)
    except KeyboardInterrupt:
        pass