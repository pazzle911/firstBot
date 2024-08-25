import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6630999471:AAEL7ztdzQHZZHqgghAVjeUo3FeEw-ziCkU')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Нажми на меня', url='https://dzen.ru/a/ZGxSRxaUPVzrbbri')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete photo')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Красота!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete photo':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)




bot.infinity_polling()
