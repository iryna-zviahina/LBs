from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import asyncio

# логування, щоб не пропустити важливі сповіщення
logging.basicConfig(level=logging.INFO)

# створення об'єкта бота і диспетчера
bot = Bot(token='Please insert here your Bot Token')
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.reply("You've started the bot!"
                        "To see all the available options click /menu")


@dp.message(Command('menu'))
async def menu(message: types.Message):
    await message.reply("Here's the menu:\n"
                        "/whisper - returns your message in the lowercase\n"
                        "/scream - returns your message in the uppercase\n"
                        "/menu - shows all of the options")


@dp.message(Command('whisper'))
async def whisper(message: types.Message):
    user_text = message.text.removeprefix('/whisper').strip()
    if not user_text:
        await message.reply("Please enter some text after the /whisper command")
        return
    await message.reply(user_text.lower())


@dp.message(Command('scream'))
async def scream(message: types.Message):
    user_text = message.text.removeprefix('/scream').strip()
    if not user_text:
        await message.reply("Please enter some text after the /scream command")
        return
    await message.reply(user_text.upper())


async def main():
    await dp.start_polling(bot)


# запуск бота
if __name__ == '__main__':
    asyncio.run(main())
