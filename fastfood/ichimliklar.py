from aiogram.types import *
#uzb
InIchimliklarUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥂Sovuq", callback_data="sovuq_uz"),
            InlineKeyboardButton(text="🥂Issiq", callback_data="issiq_uz")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_ichimlik_uz")
        ]
    ],
)

InSovuqUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Coca Cola 0.5", callback_data="coca_cola_05_uz"),
            InlineKeyboardButton(text="Coca Cola 1.0", callback_data="coca_cola_1_uz")
        ],
        [
            InlineKeyboardButton(text="Coca Cola 1.5", callback_data="coca_cola_1.5_uz"),
            InlineKeyboardButton(text="Sok", callback_data="sok_uz")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_sovuq_uz"),
            InlineKeyboardButton(text="🗑Savatchani bo'shatish", callback_data="savatcha_uz")
        ]
    ],
)

InIssiqUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Choy", callback_data="choy_uz"),
            InlineKeyboardButton(text="Limonli choy", callback_data="limonli_choy_uz")
        ],
        [
            InlineKeyboardButton(text="Cofee", callback_data="cofee_uz"),
            InlineKeyboardButton(text="Americano", callback_data="americano_uz")
        ],
        [
            InlineKeyboardButton(text="Capuchino", callback_data="capuchino_uz"),
            InlineKeyboardButton(text="Espresso", callback_data="espresso_uz")
        ],
        [
            InlineKeyboardButton(text="Latte", callback_data="latte_uz")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_issiq_uz"),
            InlineKeyboardButton(text="🗑Savatchani bo'shatish", callback_data="savatcha_uz")
        ]
    ],
)

InCola05Uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-"),
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="+", callback_data="+")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_cola_uz")
        ]
    ],
)

InCola10Uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-"),
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="+", callback_data="+")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_cola_uz")
        ]
    ],
)

InCola15Uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-"),
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="+", callback_data="+")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_cola_uz")
        ]
    ],
)

InSokUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-"),
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="+", callback_data="+")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_cola_uz")
        ]
    ],
)

InChoyUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-choy_uz"),
            InlineKeyboardButton(text="1", callback_data="1choy_uz"),
            InlineKeyboardButton(text="+", callback_data="+choy_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)

InLimonliUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-limonli_uz"),
            InlineKeyboardButton(text="1", callback_data="1limonli_uz"),
            InlineKeyboardButton(text="+", callback_data="+limonli_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)

InCofeeUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-cofee_uz"),
            InlineKeyboardButton(text="1", callback_data="1cofee_uz"),
            InlineKeyboardButton(text="+", callback_data="+cofee_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)

InAmericanoUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-americano_uz"),
            InlineKeyboardButton(text="1", callback_data="1americano_uz"),
            InlineKeyboardButton(text="+", callback_data="+americano_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)

InCapuchinoUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-capuchino_uz"),
            InlineKeyboardButton(text="1", callback_data="1capuchino_uz"),
            InlineKeyboardButton(text="+", callback_data="+capuchino_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)

InEspressoUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-espresso_uz"),
            InlineKeyboardButton(text="1", callback_data="1espresso_uz"),
            InlineKeyboardButton(text="+", callback_data="+espresso_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)

InLatteUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="-latte_uz"),
            InlineKeyboardButton(text="1", callback_data="1latte_uz"),
            InlineKeyboardButton(text="+", callback_data="+latte_uz")
        ],
        [
            InlineKeyboardButton(text="💰To'lov qilish", callback_data="To'lov_qilish")
        ],
        [
            InlineKeyboardButton(text="🛒Savatchaga qo'shish", callback_data="Savatchani_bo'shatish")
        ],
        [
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_choy_uz")
        ]
    ],
)



#rus
InIchimliklarRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥂Холодно", callback_data="sovuq_rus"),
            InlineKeyboardButton(text="🥂Горячий", callback_data="issiq_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_rus")
        ]
    ],
)

InSovuqRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кока-Кола 0.5", callback_data="kkk05")
        ],
        [
            InlineKeyboardButton(text="Сок", callback_data="sok_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_sovuq_rus"),
            InlineKeyboardButton(text="🗑Очистка корзины", callback_data="savatcha_rus")
        ]
    ],
)

InIssiqRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Чай", callback_data="choy_rus"),
            InlineKeyboardButton(text="Чай с лимоном", callback_data="limonli_choy_rus")
        ],
        [
            InlineKeyboardButton(text="Кофе", callback_data="cofee_rus"),
            InlineKeyboardButton(text="Американо", callback_data="americano_rus")
        ],
        [
            InlineKeyboardButton(text="Капучино", callback_data="capuchino_rus"),
            InlineKeyboardButton(text="Эспрессо", callback_data="espresso_rus")
        ],
        [
            InlineKeyboardButton(text="Латте", callback_data="latte_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_issiq_rus"),
            InlineKeyboardButton(text="🗑Очистка корзины", callback_data="savatcha_rus")
        ]
    ],
)


InCola05Rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_cola_rus")
        ]
    ],
)

InCola10Rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_cola_rus")
        ]
    ],
)

InCola15Rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_cola_rus")
        ]
    ],
)

InSokRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="orqaga_cola_rus")
        ]
    ],
)


InChoyRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)

InCofeeRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)

InLimonliChoyRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)

InAmericanoRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)

InLatteRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)

InCapuchinoRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)

InEspressoRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="mm"),
            InlineKeyboardButton(text="1", callback_data="bb"),
            InlineKeyboardButton(text="+", callback_data="hh")
        ],
        [
            InlineKeyboardButton(text="💰Оплата", callback_data="to'lov_qilish_rus")
        ],
        [
            InlineKeyboardButton(text="🛒Добавить в корзину", callback_data="savatchani_bo'shatish_rus")
        ],
        [
            InlineKeyboardButton(text="⬅Назад", callback_data="orqaga_choy_rus")
        ]
    ],
)
