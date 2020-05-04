from telebot import types
import config
def generate_vadim():
    markup = types.InlineKeyboardMarkup()
    for player_ans, vadim_ans in zip(config.player_ans_list, config.vadim_ans_list):
        markup.add(types.InlineKeyboardButton(player_ans, callback_data=vadim_ans))
    return markup