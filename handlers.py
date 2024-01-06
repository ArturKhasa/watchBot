from config import bot
from telebot import types
from watch import Watch


def registerOrder(message):
    with open('orders.txt', 'r') as f:
        orders = f.read().split(';')
    if message.text in orders:
        bot.send_message(message.from_user.id, 'Такой заказ уже вбивали')
    else:
        with open('orders.txt', 'a') as f:
            f.write("{};".format(message.text))
        bot.send_message(message.from_user.id, 'Принято')

    prepareWishes(message)


def prepareWishes(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("Быстро", callback_data='fast')
    btn2 = types.InlineKeyboardButton("Индивидуально", callback_data='ind')
    btn3 = types.InlineKeyboardButton("Рандом", callback_data='rand')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Делаем по пожеланиям или на усмотрение дизайнера?",
                     reply_markup=markup)


def prepareFast(message):
    bot.send_message(message.chat.id,
                     text="Что пишем на циферблате над стрелками?(Чтобы ничего не писать введите 0)")
    # TODO: Отправка рандомно собранного изображения с часами и текстом из сообшения


def prepateInd(message):
    watch = Watch()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Черный")
    btn2 = types.KeyboardButton("Белый")
    btn3 = types.KeyboardButton("Картинку")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Цвет циферблата?",
                     reply_markup=markup)
    bot.register_next_step_handler(message, setColor, watch)


def setColor(message, watch):
    if message.text == 'Черный':
        watch.color = 'black'
    elif message.text == 'Белый':
        watch.color = 'white'
    elif message.text == 'Картинку':
        watch.color = 'image'
    else:
        bot.send_message(message.chat.id,
                         text="Неизвестный параметр")
        bot.register_next_step_handler(message, setColor, watch)


def prepareFace(watch):
    pass


def setWatchFace(message, watch):
    pass
