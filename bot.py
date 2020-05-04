import telebot
import config
import utils
from telebot import types

bot = telebot.TeleBot(config.token)
'''
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)'''

@bot.message_handler(commands=['enter'])
def vadim(message):
    markup = utils.generate_vadim(config.player_ans_list)
    bot.send_message(message.chat.id, config.vadim_question, reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def resolve_answer(message):
    keyboard_hider = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, config.vadim_ans_list[config.player_ans_list.index(message.text)],
                     reply_markup=keyboard_hider)

	
if __name__ == '__main__':
    bot.infinity_polling()