from aiogram.types import *

"""Uzbekcha inline"""
Instart = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="uzb_til"),
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="rus_til")
        ]
    ],
)

InMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍔 Burger", callback_data="Burger"),
            InlineKeyboardButton(text="🌯 Lavash", callback_data="Lavash")
        ],
        [
            InlineKeyboardButton(text="🍕 Pizza", callback_data="Pizza"),
            InlineKeyboardButton(text="🥂 Ichimliklar", callback_data="Ichimliklar")
        ],
        [
            InlineKeyboardButton(text="🚪Orqaga", callback_data="orqaga_inMenyuga")
        ]
    ],
)

"""Ruscha inline"""

InMenuRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍔 Бургер", callback_data="burger_rus"),
            InlineKeyboardButton(text="🌯 Лаваш", callback_data="lavash_rus")
        ],
        [
            InlineKeyboardButton(text="🍕 Пицца", callback_data="pizza_rus"),
            InlineKeyboardButton(text="🥂 Напитки", callback_data="ichimliklar_rus")
        ],
        [
            InlineKeyboardMarkup(text="🚪Назад", callback_data="Orqaga_rus")
        ]
    ],
)
