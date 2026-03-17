import asyncio

import logging

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession

from config import TOKEN_API
from handlers import router

#session = AiohttpSession(proxy="http://proxy.server:3128")

bot = Bot(token=TOKEN_API,) #session=session)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was successfully finished")
