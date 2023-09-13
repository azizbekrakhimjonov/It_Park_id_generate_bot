import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

token = "6384532641:AAF0e8iMw_ZNb1HGqkr8Kz3-X5KsRPyCgTQ"

bot = Bot(token=token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    upload_name = State()
    upload_description = State()
    upload_price = State()
    upload_photo = State()


@dp.message_handler(commands='up')
async def upload(message: types.Message):
    await FSMAdmin.upload_name.set()
    await message.answer('Напиши название')


@dp.message_handler(state=FSMAdmin.upload_name)
async def upload_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Теперь отправь описание')


@dp.message_handler(state=FSMAdmin.upload_description)
async def upload_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer('Теперь отправь цену')


@dp.message_handler(state=FSMAdmin.upload_price)
async def upload_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMAdmin.next()
    await message.answer('Теперь отправь фото')


@dp.message_handler(content_types=['photo'], state=FSMAdmin.upload_photo)
async def upload_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text('Name: ', md.bold(data['name'])),
            md.text('Description: ', md.code(data['description'])),
            md.text('Price :', data['price']),
            md.text('Photo id ', data['photo'])
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    await message.answer('Готово!')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)