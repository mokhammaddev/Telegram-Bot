import logging
from aiogram import executor
from config import dp
from inline import *
from reply import *
from burger import *
from lavash import *
from pizza import *
from ichimliklar import *
logging.basicConfig(level=logging.INFO)

"""Start qismi"""


@dp.message_handler(commands='start')
async def start(msg: Message):
    await msg.answer(f"<b>Assalomu alekum {msg.from_user.full_name}</b>\n"
                     f"<b>Привет {msg.from_user.full_name}</b>", parse_mode='html')
    await msg.answer(f"<b>Iltimos tilni tanlang</b>\n"
                     f"<b>Пожалуйста, выберите язык</b>", parse_mode='html', reply_markup=Instart)
    # await msg.delete()

""" Uzbekcha til"""
@dp.callback_query_handler(text_contains="uzb_til")
async def uzb_tili(call: CallbackQuery):
    await call.message.answer(f"📞 Nomer", reply_markup=menuRaqamUz)
    # await call.message.delete()
    await call.answer(cache_time=30)

@dp.message_handler(text="📥 Davom etish")
async def davom_etish(msg: Message):
    await msg.answer(f"<b>Davom etish</b>", parse_mode='html', reply_markup=menuKirishUz)
    # await msg.delete()

"""Menyu qismi"""
@dp.message_handler(text="🍔 Menu 🍔")
async def menu(msg: Message):
    await msg.answer_photo(open("image/Fastfood_menu.jpg", "rb"), f"<b>Menu...</b>", parse_mode='html', reply_markup=InMenu)
    # await msg.delete()

@dp.callback_query_handler(text="Orqaga")
async def orqaga(call: CallbackQuery):
    await call.message.answer(f"<b>Orqaga...</b>", parse_mode='html', reply_markup=menuKirishUz)
    # await call.message.delete()
    await call.answer(cache_time=30)

@dp.message_handler(text="🗑 Savatchani bo'shatish")
async def savatchani_boshatish(msg: Message):
    await msg.answer(f"<i><b>Savatcha bo'shatildi!</b></i>", parse_mode='html', reply_markup=menuKirishUz)

"""Burger qismi"""
@dp.callback_query_handler(text="Burger")
async def burgeruz(call: CallbackQuery):
    img = open("image/burger malumotlar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Burger...</b>", parse_mode='html', reply_markup=InBurgerUz)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="cheese_burger_uz")
async def cheeseburgeruz(call: CallbackQuery):
    img = open("image/Cheeseburger.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Cheese Burger\n"
                                         f"Narx: 22000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InCheeseBurgerUz)
    await call.message.delete()
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="hamburger_uz")
async def hamburgeruz(call: CallbackQuery):
    img = open("image/hamburger.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Hamburger\n"
                                         f"Narx: 20000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InHamBurgerUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="goshtsiz_burger_uz")
async def goshtsiz_burger_uz(call: CallbackQuery):
    img = open("image/Taco.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Taco...</b>", parse_mode='html', reply_markup=InGoshtsizBurgerUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="burger_haqida")
async def burger_haqida(call: CallbackQuery):
    # img = open("image/burger malumotlar.jpg", "rb")
    await call.message.answer(burgertext, reply_markup=InBurgerUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_burger_uz")
async def orqaga_burger_uz(call: CallbackQuery):
    await call.message.answer(f"<b>Orqaga.................</b>", parse_mode='html', reply_markup=InBurgerUz)
    await call.message.delete()
    await call.answer(cache_time=30)

"""Lavash qismi"""
@dp.callback_query_handler(text_contains="Lavash")
async def lavashuz(call: CallbackQuery):
    img = open("image/lavash haqida malumot.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Lavash...</b>", parse_mode='html', reply_markup=InLavashUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="orqaga_lavash_uz")
async def orqaga_lavash_uz(call: CallbackQuery):
    await call.message.answer(f"<i><b>Orqaga</b></i>", parse_mode='html', reply_markup=InLavashUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="lavash_oddiy")
async def lavashshuz(call: CallbackQuery):
    img = open("image/lavash oddiy.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Lavash\n"
                                         f"Narx: 25000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InLavash1Uz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="big_lavash")
async def big_lavash_uz(call: CallbackQuery):
    img = open("image/lavash katta.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Big Lavash"
                                         f"Narx: 32000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InLavashBigUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="big_lavash_sir")
async def big_lavash_sir_uz(call: CallbackQuery):
    img = open("image/sirli lavash.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Big Lavash Sirli\n"
                                         f"Narx: 35000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InLavashBigSirliUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="lavash_haqida")
async def lavash_haqida(call: CallbackQuery):
    # img = open("image/lavash haqida malumot.jpg", "rb")
    await call.message.answer(lavashtext, reply_markup=InLavashUz)
    await call.message.delete()
    await call.answer(cache_time=30)

"""Pizza qismi"""
@dp.callback_query_handler(text_contains="Pizza")
async def pizza(call: CallbackQuery):
    img = open("image/pitsa malumot.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Pizza...</b>", parse_mode='html', reply_markup=InPizzaUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_danar")
async def pizza_danar(call: CallbackQuery):
    img = open("image/pizza danar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Pizza Danar 40sm\n"
                                         f"Narx: 99000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InPizzaDanarUz)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="pizza_mevali")
async def pizza_mevali(call: CallbackQuery):
    img = open("image/mevali pi.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Pizza Mevali 40sm\n"
                                    f"Narx: 99000.00 сум\n"
                                    f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InPizzaMevaliUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_qoziqorin")
async def pizza_qoziqorin(call: CallbackQuery):
    img = open("image/qo'ziqorinli pizza.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Qo'ziqorinli Pizza 40 sm\n"
                                         f"Narx: 85000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InPizzaQoziqorinUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_haqida")
async def pizza_haqida(call: CallbackQuery):
    # img = open("image/pitsa malumot.jpg", "rb")
    await call.message.answer(pizzatext, reply_markup=InPizzaUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_pizza_uz")
async def orqaga_pizza_uz(call: CallbackQuery):
    await call.message.answer(f"<b>Orqaga....</b>", parse_mode='html', reply_markup=InPizzaUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="orqaga_uz")
async def orqagaa(call: CallbackQuery):
    img = open("image/Fastfood_menu.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Orqaga....</b>", parse_mode='html', reply_markup=InMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

"""Ichimliklar"""
@dp.callback_query_handler(text="Ichimliklar")
async def ichimliklar(call: CallbackQuery):
    img = open("image/ichimliklar.jpg", "rb")
    await call.message.answer_photo(img, f"<i><b>Ichimliklar</b></i>",parse_mode='html', reply_markup=InIchimliklarUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="sovuq_uz")
async def sovuq_uz(call: CallbackQuery):
    await call.message.answer(f"<b>Sovuq..</b>", parse_mode='html', reply_markup=InSovuqUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="issiq_uz")
async def issiq_uz(call: CallbackQuery):
    await call.message.answer(f"<b>Issiq...</b>", parse_mode='html', reply_markup=InIssiqUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_ichimlik_uz")
async def orqaga_ichimlik_uz(call: CallbackQuery):
    img = open("image/Fastfood_menu.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Orqaga....</b>", parse_mode='html', reply_markup=InMenu)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="coca_cola_05_uz")
async def coca_cola_05_uz(call: CallbackQuery):
    img = open("image/Coca Cola 05.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Coca Cola 0.5 l\n"
                                         f"Narx: 9000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InCola05Uz)
    await call.message.delete()
    await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="-cola05_uz")
# async def cola05_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Cola Cola 0.5 litr olib tashlandi</i>", parse_mode='html', reply_markup=InCola05Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="1cola05_uz")
# async def cola05_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>Cola Cola 0.5 litr qabul qilindi</i>", parse_mode='html', reply_markup=InCola05Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
#
# @dp.callback_query_handler(text="+cola05_uz")
# async def cola05_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Cola Cola 0.5 litr qo'shildi</i>", parse_mode='html', reply_markup=InCola05Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)

@dp.callback_query_handler(text="coca_cola_1_uz")
async def coca_cola_1_uz(call: CallbackQuery):
    img = open("image/cola 15.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Coca Cola 1,0л.\n"
                                         f"Narx: 12000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :\n</b>", parse_mode='html', reply_markup=InCola10Uz)
    await call.answer(cache_time=30)

# @dp.callback_query_handler(text="+cola10_uz")
# async def cola10_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Cola Cola 1 litr qo'shildi</i>", parse_mode='html', reply_markup=InCola10Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="-cola10_uz")
# async def cola10_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Cola Cola 1 litr olib tashlandi</i>", parse_mode='html', reply_markup=InCola10Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="1cola10_uz")
# async def cola10_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>Cola Cola 1 litr qabul qilindi</i>", parse_mode='html', reply_markup=InCola10Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)

@dp.callback_query_handler(text="coca_cola_1.5_uz")
async def coca_cola_15_uz(call: CallbackQuery):
    img = open("image/cola 15.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Coca Cola 1,5л.\n"
                                    f"Narx: 15000.00 сум\n"
                                    f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InCola15Uz)
    await call.message.delete()
#     await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="+cola15_uz")
# async def cola15_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Cola Cola 1.5 litr qo'shildi</i>", parse_mode='html', reply_markup=InCola15Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="-cola15_uz")
# async def cola15_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Cola Cola 1.5 litr olib tashlandi</i>", parse_mode='html', reply_markup=InCola15Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="1cola15_uz")
# async def cola15_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>Cola Cola 1.5 litr qabul qilindi</i>", parse_mode='html', reply_markup=InCola15Uz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#

@dp.callback_query_handler(text="sok_uz")
async def sok_uz(call: CallbackQuery):
    img = open("image/sok.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Sok......\n"
                                         f"Narx: 13000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InSokUz)
    await call.message.delete()
    await call.answer(cache_time=30)

#
# @dp.callback_query_handler(text="+sok_uz")
# async def sok_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Sok qo'shildi</i>", parse_mode='html', reply_markup=InSokUz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
#
# @dp.callback_query_handler(text="-sok_uz")
# async def sok_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>1 ta Sok olib tashlandi</i>", parse_mode='html', reply_markup=InSokUz)
#     await call.message.delete()
#     await call.answer(cache_time=30)
#
#
# @dp.callback_query_handler(text="1sok_uz")
# async def sok_uz(call: CallbackQuery):
#     await call.message.answer(f"<i>Sok qabul qilindi</i>", parse_mode='html', reply_markup=InSokUz)
#     await call.message.delete()
#     await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="1")
async def qabul_qilindi(call: CallbackQuery):
    await call.answer("Qabul qilindi!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="-")
async def ayirish(call: CallbackQuery):
    await call.answer("Bitta bururtma olib tashlandi!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="+")
async def qoshish(call: CallbackQuery):
    await call.answer("Bitta buyurtma qo'shildi", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="orqaga_inMenyuga")
async def orqaga(call: CallbackQuery):
    await call.message.answer(f"<b>Orqaga........</b>", parse_mode='html', reply_markup=menuKirishUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_sovuq_uz")
async def orqaga_sovuq_uz(call: CallbackQuery):
    img = open("image/ichimliklar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>⬅Orqaga.....</b>", parse_mode='html', reply_markup=InIchimliklarUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="choy_uz")
async def choy_uz(call: CallbackQuery):
    img = open("image/choy.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Чай\n"
                                         f"Narx: 3000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InChoyUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="limonli_choy_uz")
async def limonli_choy_uz(call: CallbackQuery):
    img = open("image/choy limon.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Limonli choy\n"
                              f"Narx: 8000.00 сум\n"
                              f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InLimonliUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="cofee_uz")
async def cofee_uz(call: CallbackQuery):
    img = open("image/kofe.jpg", "rb")
    await call.message.answer_photo(img, f"<b>cofee\n"
                              f"Narx: 7000.00 сум\n"
                              f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InCofeeUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="americano_uz")
async def americano_uz(call: CallbackQuery):
    img = open("image/americano.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Americano\n"
                              f"Narx: 12000.00 сум\n"
                              f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InAmericanoUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="capuchino_uz")
async def capuchino_uz(call: CallbackQuery):
    img = open("image/capichino.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Kapichino\n"
                              f"Narx: 12000.00 сум\n"
                              f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InCapuchinoUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="espresso_uz")
async def espresso_uz(call: CallbackQuery):
    img = open("image/espresso.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Espresso\n"
                              f"Narx: 10000.00 сум\n"
                              f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InEspressoUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="latte_uz")
async def latte_uz(call: CallbackQuery):
    img = open("image/latte.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Latte\n"
                                         f"Narx: 10000.00 сум\n"
                                         f"Sonini tanlang yoki kiriting :</b>", parse_mode='html', reply_markup=InLatteUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_issiq_uz")
async def orqaga_issiq_uz(call: CallbackQuery):
    img = open("image/ichimliklar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>⬅Orqaga.....</b>", parse_mode='html', reply_markup=InIchimliklarUz)
    await call.message.delete()
    await call.answer(cache_time=30)
#
# @dp.callback_query_handler(text="orqaga_sovuq_uz")
# async def orqaga_issiq_uz(call: CallbackQuery):
#     await call.message.answer(f"<b>Orqaga....</b>", parse_mode='html', reply_markup=InIchimliklarUz)

@dp.callback_query_handler(text="orqaga_choy_uz")
async def orqaga_issiq(call: CallbackQuery):
    await call.message.answer(f"<b>Orqaga...</b>", parse_mode='html', reply_markup=InIssiqUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_cola_uz")
async def orqaga_sovuq(call: CallbackQuery):
    await call.message.answer(f"<b>Orqaga....</b>", parse_mode='html', reply_markup=InSovuqUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="To'lov_qilish")
async def tolov_qilish(call: CallbackQuery):
    await call.answer("To'lov qilindi!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="Savatchani_bo'shatish")
async def savatchani_boshatish(call: CallbackQuery):
    await call.answer("Savatchaga qo'shildi!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="savatcha_uz")
async def savatcha_uz(call: CallbackQuery):
    await call.answer("Savatchadan bo'shatildi!", cache_time=30, show_alert=True)

"""Asosiy menu"""
@dp.callback_query_handler(text_contains="Asosiy_menu_uz")
async def asosiy_menu(call: CallbackQuery):
    await call.message.answer(f"<b>Asosiy menu...</b>", parse_mode='html', reply_markup=InMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="Asosiy_menu_ru")
async def asosiy_menu(call: CallbackQuery):
    await call.message.answer(f"<b>🍔 Меню 🍔...</b>", parse_mode='html', reply_markup=InMenuRus)
    await call.message.delete()
    await call.answer(cache_time=30)

"""Izoh qoldirish"""
@dp.message_handler(text="✍ Izoh qoldirish")
async def izoh(msg: Message):
    await msg.answer(f"<b>Izoh qoldirish</b>", parse_mode='html', reply_markup=menuIzoh)
    # await msg.delete()

@dp.message_handler(text="🙂Qoniqarli")
async def qoniqarli(msg: Message):
    await msg.answer(f"<b>Izoh uchun rahmat</b>", parse_mode='html', reply_markup=menuKirishUz)
    # await msg.delete()

@dp.message_handler(text="😃Yaxshi")
async def qoniqarli(msg: Message):
    await msg.answer(f"<b>Izoh uchun rahmat</b>", parse_mode='html', reply_markup=menuKirishUz)
    # await msg.delete()

@dp.message_handler(text="😁A'lo")
async def qoniqarli(msg: Message):
    await msg.answer(f"<b>Izoh uchun rahmat</b>", parse_mode='html', reply_markup=menuKirishUz)
    # await msg.delete()

"""Sozlamalar"""
@dp.message_handler(text="⚙ Tilni almashtirish🇺🇿")
async def sozlamalar(msg: Message):
    await msg.answer(f"<b>Sozlamalar</b>", parse_mode='html', reply_markup=Instart)
    await msg.delete()

"""Ruscha tili"""
@dp.callback_query_handler(text_contains="rus_til")
async def rus_tili(call: CallbackQuery):
    await call.message.answer(f"<b>📞 Номер</b>", parse_mode='html', reply_markup=menuRaqamRus)
    # await call.message.delete()
    await call.answer(cache_time=30)

@dp.message_handler(text="📥 Продолжать")
async def otkazish(msg: Message):
    await msg.answer(f"<i><b>Продолжать...</b></i>", parse_mode='html', reply_markup=menuKirishRus)

"""Menyu qismi"""
@dp.message_handler(text="🍔 Меню 🍔")
async def menu(msg: Message):
    await msg.answer_photo(open("image/Fastfood_menu.jpg", "rb"), f"<b>Меню...</b>", parse_mode='html', reply_markup=InMenuRus)
    # await msg.delete()

"""Burger qismi"""
@dp.callback_query_handler(text="burger_rus")
async def burgerrus(call: CallbackQuery):
    img = open("image/burger malumotlar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Бургер...</b>", parse_mode='html', reply_markup=InBurgerRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="Hamburger_rus")
async def Hamburger_ru(call: CallbackQuery):
    img = open("image/hamburger.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Гамбургер\n"
                              f"Цена: 20000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InHamBurgerRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="goshtsiz_burger_rus")
async def goshtsiz_burger_ru(call: CallbackQuery):
    img = open("image/Taco.jpg", "rb")
    await call.message.answer_photo(img, f"<b>🌮Тако\n"
                                         f"Цена: 25000.00 сум\n"
                                         f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InGoshtsizBurgerRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="cheese_burger_rus")
async def cheese_burger_ru(call: CallbackQuery):
    img = open("image/cheeseburger.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Чизбургер\n"
                                         f"Цена: 22000.00 сум\n"
                                         f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InCheeseBurgerRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_burger_rus")
async def orqaga_pizza_rus(call: CallbackQuery):
    img = open("image/burger malumotlar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Назад</b>", parse_mode='html', reply_markup=InBurgerRus)
    await call.message.delete()
    await call.answer(cache_time=30)

"""Lavash qismi"""
@dp.callback_query_handler(text="lavash_rus")
async def lavash(call: CallbackQuery):
    img = open("image/lavash haqida malumot.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Лаваш...</b>", parse_mode='html', reply_markup=InLavashRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="lavashsh_rus")
async def lavashsh_rus(call: CallbackQuery):
    img = open("image/lavash oddiy.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Лаваш\n"
                              f"Цена: 25000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InLavash1Rus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="big_lavash_rus")
async def big_lavash_rus(call: CallbackQuery):
    img = open("image/lavash katta.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Большой лаваш\n"
                              f"Цена: 30000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InLavashBigRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="big_lavash_sir_rus")
async def big_lavash_sir_rus(call: CallbackQuery):
    img = open("image/biglavash sirli .png", "rb")
    await call.message.answer(f"<b>Большой лаваш с сыром/n"
                              f"Цена: 25000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InLavashBigSirliRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_lavash_rus")
async def orqaga_pizza_rus(call: CallbackQuery):
    img = open("image/lavash haqida malumot.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Назад</b>", parse_mode='html', reply_markup=InLavashRus)
    await call.message.delete()
    await call.answer(cache_time=30)

"""Pizza qismi"""
@dp.callback_query_handler(text="pizza_rus")
async def pizza(call: CallbackQuery):
    img = open("image/pitsa malumot.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Пицца...</b>", parse_mode='html', reply_markup=InPizzaRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_danar_rus")
async def pizza_danar_rus(call: CallbackQuery):
    img = open("image/pizza danar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Данарская пицца 40см\n"
                                         f"Цена: 99000.00 сум\n" 
                                         f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InPizzaDanarUz)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_mevali_rus")
async def pizza_mevali_rus(call: CallbackQuery):
    img = open("image/mevali pi.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Фруктовая пицца 40см\n"
                              f"Цена: 89000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InPizzaMevaliRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_qoziqorin_rus")
async def pizza_qoziqorin_rus(call: CallbackQuery):
    img = open("image/qo'ziqorinli pizza.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Пицца с грибами 40см\n"
                                         f"Цена: 85000.00 сум\n"
                                         f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InPizzaQoziqorinRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_pizza_rus")
async def orqaga_pizza_rus(call: CallbackQuery):
    img = open("image/pitsa malumot.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Назад</b>", parse_mode='html', reply_markup=InPizzaRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="ichimliklar_rus")
async def ichimliklar_rus(call: CallbackQuery):
    img = open("image/ichimliklar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>🥂 Напитки....</b>", parse_mode='html', reply_markup=InIchimliklarRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="sovuq_rus")
async def sovuq_rus(call: CallbackQuery):
    await call.message.answer(f"<b>🥂Холодно.....</b>", parse_mode='html', reply_markup=InSovuqRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="issiq_rus")
async def issiq_rus(call: CallbackQuery):
    await call.message.answer(f"<b>🥂Горячий.....</b>", parse_mode='html', reply_markup=InIssiqRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="kkk05")
async def coca_cola_05_rus(call: CallbackQuery):
    img = open("image/Coca Cola 05.jpg", "rb")
    await call.message.answer_photo(img, f"Coca Cola 0.5л.\n"
                              f"Цена: 9000.00 сум\n"
                              f"Выберите или введите количество цифрами:", parse_mode='html', reply_markup=InCola05Rus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="kkk10")
async def coca_cola_1_rus(call: CallbackQuery):
    img = open("image/cola 15.jpg", "rb")
    await call.message.answer_photo(img, f"<b>11000.00 сум\n"
                                   f"Выберите или введите количество цифрами:\n</b>", parse_mode='html', reply_markup=InCola10Rus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="kkk15")
async def coca_cola_15_rus(call: CallbackQuery):
    img = open("image/cola 15.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Coca Cola 1.5л.\n"
                              f"Цена: 14000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InCola15Rus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_sovuq_rus")
async def orqaga_sovuq_rus(call: CallbackQuery):
    await call.message.answer(f"<b>Назад.......</b>", parse_mode='html', reply_markup=InIchimliklarRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="sok_rus")
async def sok_rus(call: CallbackQuery):
    img = open("image/sok.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Сок\n"
                              f"Цена: 14000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InSokRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="choy_rus")
async def choy_rus(call: CallbackQuery):
    img = open("image/choy.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Чай\n"
                              f"Цена: 3000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="limonli_choy_rus")
async def limonli_choy_rus(call: CallbackQuery):
    img = open("image/choy limon.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Чай с лимоном\n"
                              f"Цена: 4000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="cofee_rus")
async def cofeeee_rus(call: CallbackQuery):
    img = open("image/kofe.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Кофе\n"
                              f"Цена: 7000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="americano_rus")
async def americano_rus(call: CallbackQuery):
    img = open("image/americano.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Американо\n"
                              f"Цена: 8000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="capuchino_rus")
async def capuchino_rus(call: CallbackQuery):
    img = open("image/capichino.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Капучино\n"
                              f"Цена: 9000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="latte_rus")
async def latte_rus(call: CallbackQuery):
    img = open("image/latte.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Латте\n"
                              f"Цена: 10000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="espresso_rus")
async def espresso_rus(call: CallbackQuery):
    img = open("image/espresso.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Эспрессо\n"
                              f"Цена: 9000.00 сум\n"
                              f"Выберите или введите количество цифрами:</b>", parse_mode='html', reply_markup=InChoyRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="orqaga_choy_rus")
async def orqaga_choy_rus(call: CallbackQuery):
    img = open("image/ichimliklar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>⬅Назад......</b>", parse_mode='html', reply_markup=InIssiqRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="orqaga_cola_rus")
async def orqaga_cola_rus(call: CallbackQuery):
    await call.message.answer(f"<b>Назад......</b>", parse_mode='html', reply_markup=InSovuqRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_issiq_rus")
async def orqaga_issiq_rus(call: CallbackQuery):
    img = open("image/ichimliklar.jpg", "rb")
    await call.message.answer_photo(img, f"<b>⬅Назад.....</b>", parse_mode='html', reply_markup=InIchimliklarRus)
    # await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga_rus")
async def orqaga_rus(call: CallbackQuery):
    img = open("image/Fastfood_menu.jpg", "rb")
    await call.message.answer_photo(img, f"<b>Назад</b>", parse_mode='html', reply_markup=InMenuRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="Orqaga_rus")
async def orqaga_rus(call: CallbackQuery):
    await call.message.answer(f"<b>Назад</b>", parse_mode='html', reply_markup=menuKirishRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="bb")
async def qabul_qilindi_rus(call: CallbackQuery):
    await call.answer("Принято!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="hh")
async def ayirish_rus(call: CallbackQuery):
    await call.answer("Один заказ был удален!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="mm")
async def ayirish_rus(call: CallbackQuery):
    await call.answer("Добавлен один заказ!", cache_time=30, show_alert=True)
#
# @dp.callback_query_handler(text_contains="Savatchani_bo'shatish_rus")
# async def savatchani_boshatish_rus(call: CallbackQuery):
#     await call.answer("Добавлено в корзину!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="To'lov_qilish_rus")
async def tolov_qilish_rus(call: CallbackQuery):
    await call.answer("Оплаченный!", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="savatcha_rus")
async def savatcha_rus(call: CallbackQuery):
    await call.answer("🗑Очистка корзины", cache_time=30, show_alert=True)

# """Asosiy menu"""
# @dp.callback_query_handler(text="orqaga_burger_rus")
# async def orqaga_burger_rus(call: CallbackQuery):
#     img = open("image/burger malumotlar.jpg", "rb")
#     await call.message.answer_photo(img, f"<b>Назад...</b>", parse_mode='html', reply_markup=InBurgerRus)
#     await call.message.delete()
#     await call.answer(cache_time=30)

"""Izoh qoldirish"""
@dp.message_handler(text="✍ Оставить комментарий")
async def izoh(msg: Message):
    await msg.answer(f"<b>Оставить комментарий</b>", parse_mode='html', reply_markup=menuIzohRus)

@dp.message_handler(text="🙂Удовлетворительный")
async def qoniqarli(msg: Message):
    await msg.answer(f"<b>Спасибо за комментарий</b>", parse_mode='html', reply_markup=menuKirishRus)

@dp.message_handler(text="😃Хороший")
async def qoniqarli(msg: Message):
    await msg.answer(f"<b>Спасибо за комментарий</b>", parse_mode='html', reply_markup=menuKirishRus)

@dp.message_handler(text="😁Превосходно")
async def qoniqarli(msg: Message):
    await msg.answer(f"<b>Спасибо за комментарий</b>", parse_mode='html', reply_markup=menuKirishRus)

"""Sozlamalar"""
@dp.message_handler(text="⚙ Изменение языка🇷🇺")
async def sozlamalar(msg: Message):
    await msg.answer(f"Настройки", parse_mode='html', reply_markup=Instart)

@dp.message_handler(text="🗑 Очистить корзину")
async def savatchani_boshatish_rus(message: Message):
    await message.answer(f"<i><b>🗑 Очистить корзину</b></i>", parse_mode='html', reply_markup=menuKirishRus)

@dp.callback_query_handler(text="burger_haqida_rus")
async def burger_haqida_rus(call: CallbackQuery):
    # img = open("image/burger malumotlar.jpg", "rb")
    await call.message.answer(burgertextrus, reply_markup=InBurgerRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="lavash_haqida_rus")
async def lavash_haqida_rus(call: CallbackQuery):
    # img = open("image/lavash haqida malumot.jpg", "rb")
    await call.message.answer(lavashtextrus, reply_markup=InLavashRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="pizza_haqida_rus")
async def pizza_haqida_rus(call: CallbackQuery):
    # img = open("image/pitsa malumot.jpg", "rb")
    await call.message.answer(pizzatextrus, reply_markup=InPizzaRus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="to'lov_qilish_rus")
async def tolov_qilish_rus(call: CallbackQuery):
    await call.answer("Оплаченный", cache_time=30, show_alert=True)

@dp.callback_query_handler(text_contains="savatchani_bo'shatish_rus")
async def savatchani_boshatish_rus(call: CallbackQuery):
    await call.answer("Добавлено в корзину", cache_time=30, show_alert=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
