import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import utils
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

@dp.message(Command('resize'))
async def cmd_resize(message: types.Message):
    utils.clear_folder('ModifiedImages/')
    utils.scaling_images_in_folder('OriginalImages/')
    utils.clear_folder('OriginalImages/')

    for file_name in utils.create_files_list('ModifiedImages/'):
        image = types.FSInputFile('ModifiedImages/' + file_name)
        await message.answer_document(image)
    utils.clear_folder('ModifiedImages/')

@dp.message(F.photo)
async def download_photo(message: types.Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"OriginalImages/{message.photo[-1].file_id}.png"
    )

async def main():
    utils.clear_folder('OriginalImages/')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
