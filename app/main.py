import asyncio

import logging

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession

import os
from dotenv import load_dotenv

from handlers import router


load_dotenv()

TOKEN_API = os.getenv('TOKEN_API')

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
