import asyncio
import logging

from bot_config import dispatcher, bot, database
from handlers.dialog import dialog_router
from handlers.start import start_router

async def on_startup():
    database.crate_tables()

async def  main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(dialog_router)

    dispatcher.startup.register(on_startup)

    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())