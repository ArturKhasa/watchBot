from config import bot
from handlers import registerOrder
from callbacks import callback_handler


@bot.message_handler(commands=['start'])
def menu(message):
    bot.send_message(message.chat.id, text="ID заказа?")
    bot.register_next_step_handler(message, registerOrder)


if __name__ == "__main__":
    bot.polling(none_stop=True)
