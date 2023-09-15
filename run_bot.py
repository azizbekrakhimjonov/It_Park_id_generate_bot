import asyncio
import logging
import os
import time

from aiogram import Bot, Dispatcher, types
from aiogram.types import MediaGroup, InputMediaDocument
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

# (id, fam, name, fname, user_img):

ID = None
img_name = None
umid_id = None


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
        await asyncio.sleep(1)
        await cm_start(message)
    else:
        await state.update_data(id=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Введите фамилию ученика:")



async def load_fam(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(1)
        await cm_start(message)
    else:
        await state.update_data(fam=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Введите имя ученика:")


async def load_name(message: types.Message, state: FSMContext):
    if message.text == 'Отменить заявку':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(1)
        await cm_start(message)
    else:
        await state.update_data(name=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Введите курс ученика:", reply_markup=course_button)




async def load_course(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        if message.text == 'Отменить заявку':
            await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
            await asyncio.sleep(1)
            await cm_start(message)
        else:
            await state.update_data(course=message.text.strip())
            await FSMAdmin.next()
            await message.reply("Отправьте фотографию ученика:")


async def load_photo(message: types.Message, state: FSMContext):
        if message.text == 'Отменить заявку':
            await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
            await asyncio.sleep(1)
            await cm_start(message)
        else:
            await message.photo[-1].download(destination_file=f"{img_name}.png", make_dirs=False)

            async with state.proxy() as data:
                data['photo'] = message.photo[0].file_id

            async with state.proxy() as data:
                writer_func(data['id'], data['fam'], data['name'], data['course'], f"{img_name}")

            await state.finish()
            await message.reply("Успешно! Нажмите на «Получить ID карту»", reply_markup=result)


async def load_make(message: types.Message):
    if message.text == 'Получить ID карту':
        await message.answer('Готово!', reply_markup=start_button)
        media = MediaGroup()
        media.attach(InputMediaDocument(open(f'{img_name}.pdf', 'rb')))
        await message.reply_media_group(media=media)
        print('Successfully upload')

        os.system(f'rm {img_name}.pdf')
        os.system(f'rm {img_name}.png')
        # os.system(f'rm {img_name}.jpg')
        print("Image is deleting...")

    if message.text == 'Назад':
        await message.answer('Вы вернулись в начало.', reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(1)
        await cm_start(message)


def register_handler_admin(dp1: Dispatcher):
    dp1.register_message_handler(cm_start, commands=['start'], state=None)  # start
    dp1.register_message_handler(load_id, state=FSMAdmin.id)  # id
    dp1.register_message_handler(load_fam, state=FSMAdmin.fam)  # fam
    dp1.register_message_handler(load_name, state=FSMAdmin.name)  # name
    dp1.register_message_handler(load_course, state=FSMAdmin.course)  # course
    dp1.register_message_handler(load_photo, state=FSMAdmin.photo, content_types="photo")  # photo
    dp1.register_message_handler(load_make)


if __name__ == '__main__':
    from aiogram import executor

    register_handler_admin(dp)
    executor.start_polling(dp, skip_updates=True)
