from aiogram.types import *
#uzb
InLavashUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Lavash", callback_data="lavash_oddiy"),
            InlineKeyboardButton(text="Big Lavash", callback_data="big_lavash")
        ],
        [
            InlineKeyboardButton(text="Big Lavash Sirli", callback_data="big_lavash_sir")
        ],
        [
            InlineKeyboardButton(text="Lavash haqida ma'lumot", callback_data="lavash_haqida")
        ],
        [
            InlineKeyboardButton(text="📥 Orqaga", callback_data="orqaga_uz")
        ]
    ],
)

InLavash1Uz = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_lavash_uz")
        ]
    ],
)


InLavashBigUz = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_lavash_uz")
        ]
    ],
)

InLavashBigSirliUz = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="⬅Orqaga", callback_data="orqaga_lavash_uz")
        ]
    ],
)

#rus
InLavashRus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Лаваш", callback_data="lavashsh_rus"),
            InlineKeyboardButton(text="Большой лаваш", callback_data="big_lavash_rus")
        ],
        [
            InlineKeyboardButton(text="Большой лаваш с сыром", callback_data="big_lavash_sir_rus")
        ],
        [
            InlineKeyboardButton(text="Информация о лаваше", callback_data="lavash_haqida_rus")
        ],
        [
            InlineKeyboardButton(text="📥 Назад", callback_data="orqaga_rus")
        ]
    ],
)


InLavash1Rus = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="⬅ Назад", callback_data="orqaga_lavash_rus")
        ]
        ],
)

InLavashBigRus = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="⬅ Назад", callback_data="orqaga_lavash_rus")
        ]
        ],
)


InLavashBigSirliRus = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="⬅ Назад", callback_data="orqaga_lavash_rus")
        ]
        ],
)


#------------------------------------------------------------------------------------------------------------------------

lavashtext = ("Lavash aslida qaysi xalqning milliy taomi hisoblanadi?Turkiya, Eron, Ozarbayjon, Armaniston va Qozog‘iston lavashni o‘zlarining milliy taomlari sifatida hisoblab keladilar.An’anaviy yupqa non sifatida dunyoga mashhur – lavash Armaniston, Eron, Turkiya, Qozog‘iston va Ozarbayjonda keng iste’mol qilinadi.  YuNYeSKO tashkiloti Armaniston lavashini xalqaro madaniy meros sifatida tan olgan. Bu esa yuqoridagi to‘rt davlat orasida bahs-munozarlarga sabab bo‘ldi va ular tashkilotning bu qaroridan norozi. Bu haqda “Dailysabah” nashri yozmoqda.Joriy yilning 28 noyabridan 2 dekabriga qadar Efiopiyada YuNYeSKO tashkiloti Nomoddiy madaniy merosni muhofaza qilish bo‘yicha hukumatlararo qo‘mitasining 11-majlisi bo‘lib o‘tadi. Ana shu uchrashuvda “Yupqa non tayyorlash va o‘zaro almashish madaniyati:  Lavash,  Qotirma,  Yupqa va Yufqa” deb nomlangan hujjat muhokama etiladi va mazkur taomlarning qaysi xalqqa tegishli ekani haqida yakuniy qaror e’lon qilinadi.Ma’lumotlarga qaraganda, Ozarbayjon va Turkiya Armanistonning lavashni uning milliy taomi sifatida tan olinishiga bo‘yicha so‘rovini bir necha vaqtdan buyon rad etib kelmoqda.Turkiya rasmiylarining so‘zlariga ko‘ra, lavash turk madaniyatida, jumladan to‘y marosimlarida katta o‘ringa ega. Asosan,  qishloq ayollari tomonidan tayyorlanadigan lavash pishloq, ko‘kat va go‘sht bilan iste’mol qilinadi. Turkiya bo‘ylab lavash restoranlarda ishtahani ochuvchi taom sifatida dasturxonga tortiladi.Ma’lumot o‘rnida, 2014 yilning 26 noyabrida YuNYeSKO lavashni nommoddiy meroslar ro‘yxatiga kiritgan. Lavashning tarixi juda qadimga borib taqaladi. Bunday turdagi nonni shumerlar,  bobilliklar, misrliklar, etrusklar va boshqa Yaqin Sharqda yashagan qadimgi xalqlar tayyorlagan.")
lavashtextrus = ("Национальным блюдом какого народа на самом деле является лаваш?Иран,Азербайджан,Армения и Казахстан считают лаваш своим национальным блюдом.Как традиционный тонкий хлеб,лаваш широко популярен в Армении,Иране,Турции,Казахстане и Азербайджане.Продается. ЮНЕСКО признала армянский лаваш международным культурным наследием. Это вызвало споры среди вышеуказанных четырех стран, и они недовольны таким решением организации. Об этом пишет издание «Dailysabah».С 28 ноября по 2 декабря этого года в Эфиопии пройдет 11-е заседание Межправительственного комитета ЮНЕСКО по охране нематериального культурного наследия. На этой встрече будет обсужден документ под названием «Культура приготовления тонкого хлеба и взаимообмена: лаваш, котырма, юпка и юфка» и будет оглашено окончательное решение о том, к какому народу относятся эти блюда. Просьба Турции признать лаваш своим национальным блюдом уже некоторое время отклоняется.По словам турецких официальных лиц, лаваш занимает большое место в турецкой культуре, в том числе в свадебных церемониях. Лаваш, приготовленный сельскими женщинами, в основном едят с сыром, зеленью и мясом. Лаваш подают в качестве закуски в ресторанах по всей Турции.Для справки, 26 ноября 2014 года ЮНЕСКО включила лаваш в список нематериального наследия. История лаваша уходит в далекое прошлое. Этот вид хлеба готовили шумеры, вавилоняне, египтяне, этруски и другие древние народы, жившие на Ближнем Востоке.")