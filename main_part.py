import datetime
import re

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import markups as nav
import logic as logic
from db import Database
import keys


storage = MemoryStorage()
bot = Bot(token=keys.TOKEN)
dp = Dispatcher(bot, storage=storage)

db = Database('database.db')


# состояния нетто
class AutoStatesNetto(StatesGroup):
    waiting_price = State()
    waiting_volume = State()
    waiting_age = State()
    waiting_pts = State()


# состояния брутто
class AutoStatesBrutto(StatesGroup):
    waiting_price = State()
    waiting_volume = State()
    waiting_age = State()
    waiting_pts = State()


# состояния ссылки
class AutoStatesLink(StatesGroup):
    waiting_link = State()
    waiting_pts = State()


# состояния нетто
class MotoStatesNetto(StatesGroup):
    waiting_price = State()
    waiting_volume = State()
    waiting_age = State()
    waiting_pts = State()


# состояния брутто
class MotoStatesBrutto(StatesGroup):
    waiting_price = State()
    waiting_volume = State()
    waiting_age = State()
    waiting_pts = State()


class MotoStatesLink(StatesGroup):
    waiting_link = State()
    waiting_pts = State()


# состояния нетто
class ElectroStatesNetto(StatesGroup):
    waiting_price = State()
    waiting_age = State()
    waiting_pts = State()


# состояния брутто
class ElectroStatesBrutto(StatesGroup):
    waiting_price = State()
    waiting_age = State()
    waiting_pts = State()


class ElectroStatesLink(StatesGroup):
    waiting_link = State()
    waiting_pts = State()


# состояния брутто
class ComercialStatesBrutto(StatesGroup):
    waiting_price = State()
    waiting_age = State()
    waiting_pts = State()


# состояния нетто
class ComercialStatesNetto(StatesGroup):
    waiting_price = State()
    waiting_age = State()
    waiting_pts = State()


class ComercialStatesLink(StatesGroup):
    waiting_link = State()
    waiting_pts = State()


# старт и главное меню с первым постом
@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = int(message.from_user.id)
    username_db = message.from_user.username
    if not db.user_exists(user_id):
        user_username = str(message.from_user.first_name)
        db.add_user(user_id, username_db)
        part_brutto = "<b>1. Стоимость нетто/брутто:</b>\nздесь все как с любым товаром, который вы приобретали за границей, мы рекомендуем выбирать автомобили, где возможно осуществить возврат НДС - вы и экономите, и получаете доступ к прозрачной истории обслуживания."
        part_delivery = "<b>2. Доставка</b>\nможет незначительно варьироваться от страны, но так как немецкий авторынок наиболее интересный, мы заложили в формулу стоимость исходя из доставки из Германии."
        part_math = "<b>3. Расчёт таможенных платежей</b>\nвсе наши выполненные заказы, как и ваш будущий автомобиль в целях оптимизации бюджета проходят таможенное оформление через третьи страны, входящие в ЕАЭС. "
        part_glonass = "<b>4. Получение СБКТС, ПТС, кнопки ГЛОНАСС</b>\nпока действует разрешение на эксплуатацию автомобилей без кнопки ГЛОНАСС, Вы можете выбрать два варианта получения российских документов."
        part_help = "<b>5. Чем мы можем помочь?</b>\nМы позволяем посчитать как ориентировочную стоимость автомобиля, если бы вы прошли этот путь самостоятельно, так и можем оказать услугу по его приобретению и доставке под ключ. Вы получите обе цены."
        part_qna = "Задать вопрос - <a href=''></a>\nНаш сайт - <b>В разработке!</b>\nЧат сообщества - <a href=''</a>"
        full_msg = f"{part_brutto}\n\n{part_delivery}\n\n{part_math}\n\n{part_glonass}\n\n{part_help}\n\n{part_qna}\n\n"
        first_msg = f"Привет, {user_username}, если ты решил приобрести автомобиль в Европе, давай расскажу, из чего строится его стоимость:"
        if db.get_user(user_id):
            await bot.send_message(message.from_user.id, first_msg, reply_markup=nav.mainMenu, parse_mode="HTML")
        else:
            await bot.send_message(message.from_user.id, first_msg, reply_markup=nav.mainMenu, parse_mode="HTML")
        await bot.send_message(message.from_user.id, full_msg, reply_markup=nav.firstPost, parse_mode="HTML")
    else:
        admin = db.get_admin(message.from_user.id)
        if admin == 'admin':
            user_username = str(message.from_user.first_name)
            part_brutto = "<b>1. Стоимость нетто/брутто:</b>\nздесь все как с любым товаром, который вы приобретали за границей, мы рекомендуем выбирать автомобили, где возможно осуществить возврат НДС - вы и экономите, и получаете доступ к прозрачной истории обслуживания."
            part_delivery = "<b>2. Доставка</b>\nможет незначительно варьироваться от страны, но так как немецкий авторынок наиболее интересный, мы заложили в формулу стоимость исходя из доставки из Германии."
            part_math = "<b>3. Расчёт таможенных платежей</b>\nвсе наши выполненные заказы, как и ваш будущий автомобиль в целях оптимизации бюджета проходят таможенное оформление через третьи страны, входящие в ЕАЭС. "
            part_glonass = "<b>4. Получение СБКТС, ПТС, кнопки ГЛОНАСС</b>\nпока действует разрешение на эксплуатацию автомобилей без кнопки ГЛОНАСС, Вы можете выбрать два варианта получения российских документов."
            part_help = "<b>5. Чем мы можем помочь?</b>\nМы позволяем посчитать как ориентировочную стоимость автомобиля, если бы вы прошли этот путь самостоятельно, так и можем оказать услугу по его приобретению и доставке под ключ. Вы получите обе цены."
            part_qna = "Задать вопрос - <a href=''></a>\nНаш сайт - <b>В разработке!</b>\nЧат сообщества - <a href=''></a>"
            full_msg = f"{part_brutto}\n\n{part_delivery}\n\n{part_math}\n\n{part_glonass}\n\n{part_help}\n\n{part_qna}\n\n"
            first_msg = f"Привет, {user_username}, если ты решил приобрести автомобиль в Европе, давай расскажу, из чего строится его стоимость:"
            if db.get_user(user_id):
                await bot.send_message(message.from_user.id, first_msg, reply_markup=nav.adminMenu, parse_mode="HTML")
            else:
                await bot.send_message(message.from_user.id, first_msg, reply_markup=nav.adminMenu, parse_mode="HTML")
            await bot.send_message(message.from_user.id, full_msg, reply_markup=nav.firstPost, parse_mode="HTML")
        else:
            user_username = str(message.from_user.first_name)
            part_brutto = "<b>1. Стоимость нетто/брутто:</b>\nздесь все как с любым товаром, который вы приобретали за границей, мы рекомендуем выбирать автомобили, где возможно осуществить возврат НДС - вы и экономите, и получаете доступ к прозрачной истории обслуживания."
            part_delivery = "<b>2. Доставка</b>\nможет незначительно варьироваться от страны, но так как немецкий авторынок наиболее интересный, мы заложили в формулу стоимость исходя из доставки из Германии."
            part_math = "<b>3. Расчёт таможенных платежей</b>\nвсе наши выполненные заказы, как и ваш будущий автомобиль в целях оптимизации бюджета проходят таможенное оформление через третьи страны, входящие в ЕАЭС. "
            part_glonass = "<b>4. Получение СБКТС, ПТС, кнопки ГЛОНАСС</b>\nпока действует разрешение на эксплуатацию автомобилей без кнопки ГЛОНАСС, Вы можете выбрать два варианта получения российских документов."
            part_help = "<b>5. Чем мы можем помочь?</b>\nМы позволяем посчитать как ориентировочную стоимость автомобиля, если бы вы прошли этот путь самостоятельно, так и можем оказать услугу по его приобретению и доставке под ключ. Вы получите обе цены."
            part_qna = "Задать вопрос - <a href=''></a>\nНаш сайт - <b>В разработке!</b>\nЧат сообщества - <a href=''></a>"
            full_msg = f"{part_brutto}\n\n{part_delivery}\n\n{part_math}\n\n{part_glonass}\n\n{part_help}\n\n{part_qna}\n\n"
            first_msg = f"Привет, {user_username}, если ты решил приобрести автомобиль в Европе, давай расскажу, из чего строится его стоимость:"
            if db.get_user(user_id):
                await bot.send_message(message.from_user.id, first_msg, reply_markup=nav.mainMenu, parse_mode="HTML")
            else:
                await bot.send_message(message.from_user.id, first_msg, reply_markup=nav.mainMenu, parse_mode="HTML")
            await bot.send_message(message.from_user.id, full_msg, reply_markup=nav.firstPost, parse_mode="HTML")


@dp.message_handler(commands=['calculate'], state='*')
async def calculate(message: types.Message, state: FSMContext):
    await state.finish()
    msg = 'Выберите тип транспорта:'
    msg_sended = await bot.send_message(message.from_user.id, msg, reply_markup=nav.techCheck)
    user_id = message.from_user.id
    username = message.from_user.username
    msg_id = msg_sended.message_id
    date = msg_sended.date
    chat_id = msg_sended.chat.id
    db.add_purchase(user_id, username, msg_id, date, chat_id)



@dp.message_handler(commands=['info'], state='*')
async def info(message: types.Message, state: FSMContext):
    await state.finish()
    user_username = str(message.from_user.first_name)
    part_brutto = "<b>1. Стоимость нетто/брутто:</b>\nздесь все как с любым товаром, который вы приобретали за границей, мы рекомендуем выбирать автомобили, где возможно осуществить возврат НДС - вы и экономите, и получаете доступ к прозрачной истории обслуживания."
    part_delivery = "<b>2. Доставка</b>\nможет незначительно варьироваться от страны, но так как немецкий авторынок наиболее интересный, мы заложили в формулу стоимость исходя из доставки из Германии."
    part_math = "<b>3. Расчёт таможенных платежей</b>\nвсе наши выполненные заказы, как и ваш будущий автомобиль в целях оптимизации бюджета проходят таможенное оформление через третьи страны, входящие в ЕАЭС. "
    part_glonass = "<b>4. Получение СБКТС, ПТС, кнопки ГЛОНАСС</b>\nпока действует разрешение на эксплуатацию автомобилей без кнопки ГЛОНАСС, Вы можете выбрать два варианта получения российских документов."
    part_help = "<b>5. Чем мы можем помочь?</b>\nМы позволяем посчитать как ориентировочную стоимость автомобиля, если бы вы прошли этот путь самостоятельно, так и можем оказать услугу по его приобретению и доставке под ключ. Вы получите обе цены."
    part_qna = "Задать вопрос - <a href='https://t.me/pokraska77mm'>pokraska77mm</a>\nНаш сайт - <b>В разработке!</b>\nЧат сообщества - <a href='https://t.me/+MXHHrKkTc-JmNGIy'>Автоимпорт 77</a>"
    full_msg = f"Привет, {user_username}, если ты решил приобрести автомобиль в Европе, давай расскажу, из чего строится его стоимость:\n\n{part_brutto}\n\n{part_delivery}\n\n{part_math}\n\n{part_glonass}\n\n{part_help}\n\n{part_qna}\n\n"
    await bot.send_message(message.from_user.id, full_msg, reply_markup=nav.infoPost, parse_mode="HTML")


@dp.message_handler(commands=['chat'], state='*')
async def chat(message: types.Message, state: FSMContext):
    await state.finish()
    msg = 'Чат сообщества - <a href="https://t.me/+MXHHrKkTc-JmNGIy">Автоимпорт 77</a>'
    await bot.send_message(message.from_user.id, msg, reply_markup=nav.mainMenu, parse_mode="HTML")