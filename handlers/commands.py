from email import message
from aiogram import Router, F
from aiogram.filters import Command, CommandStart 
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
)

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    description = (
        "Salam\n"
        "Добро пожаловать в наш барбершоп\n"
        "/address - Адрес барбершопа\n"
        "/contacts - Контакты\n"
        "/schedule - график работы\n"
        "price - прайc\n"
        "courses_barber - курсы на барбера\n"
        "feedback - отзывы\n"

    )
    kb = [
        [KeyboardButton(text="/address"), KeyboardButton(text="/price")],
        [KeyboardButton(text="/contacts"), KeyboardButton(text="/courses_barber")],
        [KeyboardButton(text="/schedule"), KeyboardButton(text="/feedback")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(description, reply_markup=keyboard)

@router.message(Command(commands=['address']))
async def address(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back")]]) # Кнопка назад

    await message.answer(
        "Адресс "
        "Улица Ибраимова 115 "
        "Ссылка, на карту 2ГИС - https://2gis.kg/bishkek/geo/15763234351114035/74.619759%2C42.874037?m=74.619759%2C42.873826%2F17.48 \n",
        reply_markup=keyboard
    )

@router.message(Command(commands=['contacts']))
async def contacts(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back")]]) # Кнопка назад
    await message.answer(
        "Контакты \n"
        "Тел: +996222368655 \n"
        "WhatsApp: wa.me/996222368655 \n"
        "Instagram: https://instagram.com/marshal_asanbai  \n",
        reply_markup=keyboard
    )



@router.message(Command(commands=["schedule"]))
async def schedule(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back")]]) # Кнопка назад
    await message.answer(
        "График работы\n"
        "Понедельник - Суббота с 11:00 - 22:00\n"
        "Выходной - Воскресенье",
        reply_markup=keyboard
    )

@router.message(Command(commands=['price']))
async def price(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back")]]) # Кнопка назад
    price_list = (
        "Модельная стрижка - 500 сом \n"
        "Стрижка McgGreggor Style - 1000 сом \n"
        "Стрижка Leonardo Dicaprio - 1300 сом \n"
        "Стрижка Спортивная - 400 сомов \n"
        "Стрижка Buzzcut - 2300 сомов \n"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Модельная", callback_data="model")],
        [InlineKeyboardButton(text="McgGreggor Style", callback_data="mcgreggor")],
        [InlineKeyboardButton(text="Leonardo Dicaprio", callback_data="leo")],
        [InlineKeyboardButton(text="Спортивная", callback_data="sport")],
        [InlineKeyboardButton(text="Buzzcut", callback_data="buzzcut")],
        [InlineKeyboardButton(text="Назал", callback_data="back_to_price")],
    ])

    await message.answer(price_list,reply_markup=keyboard)

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом

@router.callback_query(F.data=='model')
async def send_leo_picture(callback:CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_to_price")]]) # Кнопка назад
    await callback.message.delete()
    await callback.message.answer_photo(
        photo = FSInputFile('images/model.jpg'),
        caption =( #описание к фото
            "Стрижка  Модельная - 500 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp - +9961223456789"
            "Instagram: https://instagram.com/marshal_asanbai\n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом

@router.callback_query(F.data=='mcgreggor')
async def send_leo_picture(callback:CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_to_price")]]) # Кнопка назад
    await callback.message.delete()
    await callback.message.answer_photo(
        photo = FSInputFile('images/mcgreggor.jpg'),
        caption =( #описание к фотоStyle
            "Стрижка  McgGreggor Style - 1000 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp - +9961223456789"
            "Instagram: https://instagram.com/marshal_asanbai\n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом

@router.callback_query(F.data == "leo")
async def send_leo_picture(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_to_price")]])
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=FSInputFile("images/leo.jpg"),
        caption=(
            "Стрижка Leonardo Dicaprio - 1300 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp: wa.me/996222368655 \n"
            "Instagram: https://instagram.com/marshal_asanbai  \n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом

@router.callback_query(F.data=='sport')
async def send_leo_picture(callback:CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_to_price")]]) # Кнопка назад
    await callback.message.delete()
    await callback.message.answer_photo(
        photo = FSInputFile('images/sport.png'),
        caption =( #описание к фото
            "Стрижка  Спортивная - 400 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp - +9961223456789"
            "Instagram: https://instagram.com/marshal_asanbai\n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом

@router.callback_query(F.data=='buzzcut')
async def send_leo_picture(callback:CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_to_price")]]) # Кнопка назад
    await callback.message.delete()
    await callback.message.answer_photo(
        photo = FSInputFile('images/buzzcut.jpeg'),
        caption =( #описание к фото
            "Стрижка  Buzzcut - 2300 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp - +9961223456789"
            "Instagram: https://instagram.com/marshal_asanbai\n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом