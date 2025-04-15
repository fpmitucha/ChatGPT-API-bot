import telebot
from telebot import types

bot = telebot.TeleBot('7565587134:AAHoyiepbUxuXBjEZwL_AL1VFJ598KdhEJ0')


# напишем декоратор для получения файлом, в нашем случае фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # отправим ответным сообщение текст
    message.reply_to(message, 'какое красивое фото!)')
    # перейдём к созданию кнопок: inline buttons (кнопки возле сообщения)
    # пусть будем получать файл txt и отправлять и производить с ним махинации
    # создадим inline button
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup('Репозиторий по ссылке', url='https://github.com/fpmitucha/ChatGPT-API-bot'))
    markup.add(types.InlineKeyboardMarkup('Удалить фото', callback_data='delete'))
    markup.add(types.InlineKeyboardMarkup('Изменить текст', callback_data='edit'))
    bot.reply_to(message, 'безумно красивое фото!)', reply_markup=markup)

bot.polling(non_stop=True)
