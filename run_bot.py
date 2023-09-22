import asyncio
import logging
import os


from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

from buttons import result, cansel_button, start_button, course_button
from config import token
from functions import writer_func

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# (id, fam, name, course, user_img):

class FSMAdmin(StatesGroup):
    id = State()
    fam = State()
    name = State()
    course = State()
    photo = State()
    make = State()


async def cm_start(message: types.Message):
    await FSMAdmin.id.set()
    await message.reply("Введите ID ученика:", reply_markup=cansel_button)


async def load_id(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await cm_start(message)
    else:
        await state.update_data(id=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Введите фамилию ученика:")


async def load_fam(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await cm_start(message)
    else:
        await state.update_data(fam=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Введите имя ученика:")


async def load_name(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await cm_start(message)
    else:

        await state.update_data(name=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Введите курс ученика:", reply_markup=course_button)


async def load_course(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await cm_start(message)
    else:
        await state.update_data(course=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Отправьте фотографию ученика:", reply_markup=ReplyKeyboardRemove())


async def load_photo(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await cm_start(message)
    else:
        async with state.proxy() as data:
            _id = data["id"].replace('/', '_')
            await message.photo[-1].download(destination_file=f"{_id}.png", make_dirs=False)
            await state.update_data(photo=message.photo[0].file_id)
            writer_func(data['id'], data['fam'], data['name'], data['course'])

        await FSMAdmin.next()
        await message.reply("Успешно! Нажмите на «Получить ID карту»", reply_markup=result)


async def load_make(message: types.Message, state: FSMContext):
    if message.text == 'Получить ID карту':
        async with state.proxy() as data:
            _id = data['id'].replace('/', '_')
            try:
                print("Image is sending...")
                with open(f'{_id}.png', 'rb') as fg:
                    await bot.send_document(message.chat.id, InputFile(fg))
            except Exception as e:
                print(f"An error: {str(e)}")
                await message.answer('Ошибка при отправке фотографии', reply_markup=ReplyKeyboardRemove())
                await cm_start(message)

        await state.finish()
        await message.answer('/start', reply_markup=start_button)
        os.system(f'rm {_id}.png')
        print("Image is deleting...")



def register_handler_admin(dp1: Dispatcher):
    dp1.register_message_handler(cm_start, commands=['start'], state=None)  # start
    dp1.register_message_handler(load_id, state=FSMAdmin.id)  # id
    dp1.register_message_handler(load_fam, state=FSMAdmin.fam)  # fam
    dp1.register_message_handler(load_name, state=FSMAdmin.name)  # name
    dp1.register_message_handler(load_course, state=FSMAdmin.course)  # course
    dp1.register_message_handler(load_photo, state=FSMAdmin.photo, content_types="photo")  # photo
    dp1.register_message_handler(load_make, state=FSMAdmin.make) # make


if __name__ == '__main__':
    from aiogram import executor

    register_handler_admin(dp)
    executor.start_polling(dp, skip_updates=True)
