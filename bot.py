import telebot
import config
import utils

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['enter'])
def vadim(message):
    markup = utils.generate_vadim()
    bot.send_message(message.chat.id, config.vadim_question, reply_markup=markup)

@bot.callback_query_handler(func=lambda call : True)
def resolve_query(call):
    bot.send_message(call.message.chat.id, call.data)

	
if __name__ == '__main__':
    bot.infinity_polling()