from config import bot
from handlers import prepareFast
from handlers import prepateInd


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.message:
        if call.data == 'fast':
            prepareFast(call.message)
        elif call.data == 'ind':
            prepateInd(call.message)
