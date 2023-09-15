from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# controll
button_result = KeyboardButton('Получить ID карту')
button_start = KeyboardButton('Назад')
button_cansel = KeyboardButton('Отменить заявку')
result = ReplyKeyboardMarkup(resize_keyboard=True).add(button_result)
start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start)
cansel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cansel)


"""
Front End development 
Back End development 
Mobile Robotics 
UI/UX design 
Mobile App development
Foundation
"""
button_front = KeyboardButton('Front End development')
button_back = KeyboardButton('Back End development')
button_robotics = KeyboardButton('Mobile Robotics')
button_ui = KeyboardButton('UI/UX design')
button_mobile = KeyboardButton('Mobile App development')
button_foundation = KeyboardButton('Foundation')
course_button = ReplyKeyboardMarkup(resize_keyboard=True).\
    add(button_front).\
    add(button_back).\
    add(button_robotics).\
    add(button_ui).\
    add(button_mobile).\
    add(button_foundation).\
    add(cansel_button)