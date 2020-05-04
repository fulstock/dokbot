from telebot import types
import config
def generate_vadim(answer):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    list_items = config.player_ans_list
    for item in list_items:
        markup.add(item)
    return markup