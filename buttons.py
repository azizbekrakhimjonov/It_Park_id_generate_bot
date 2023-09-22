from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# controll
button_result = KeyboardButton('Получить ID карту')
button_start = KeyboardButton('/start')
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
button_front = KeyboardButton('Frontend development')
button_back = KeyboardButton('Backend development')
button_robotics = KeyboardButton('Mobile Robotics')
button_ui = KeyboardButton('UI/UX')
button_mobile = KeyboardButton('Mobile App development')
button_foundation = KeyboardButton('Foundation')
course_button = ReplyKeyboardMarkup(resize_keyboard=True).\
    add(button_front).\
    add(button_back).\
    add(button_robotics).\
    add(button_ui).\
    add(button_mobile).\
    add(button_foundation).add(button_cansel)
