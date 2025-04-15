import webbrowser

import telebot

# добавляем бота в наш проект
bot = telebot.TeleBot('7565587134:AAHoyiepbUxuXBjEZwL_AL1VFJ598KdhEJ0')


# делаем обработку программы старт
# прописываем декоратор для функции
# в аргументах прописываем на какую команду будет реагировать бот
@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    # отправляем сообщение с помощью метода send_message, в параметрах указываем айди чата с помощью метода chat.id и пишем сообщение
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['help'])
def help(message):
    # отправляем сообщение с помощью метода send_message, в параметрах указываем айди чата с помощью метода chat.id и пишем сообщение
    bot.send_message(message.chat.id, 'Help information!')
    # можно парсить строку, передав третий аргумент
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>!', parse_mode='html')


@bot.message_handler(commands=['user'])
def user_information(message):
    # посмотрим, что выведет, если передать в метод send_message сообщение, которое написал юзер
    bot.send_message(message.chat.id, f'Из этого сообщения можно получить всю информацию о тебе:\n\n {message})')
    # получим имя пользователя, фамилию и айди
    bot.send_message(message.chat.id,
                     f'Вот, например \nТвоё имя: {message.from_user.first_name}, фамилия: {message.from_user.last_name}, id: {message.from_user.id}')


@bot.message_handler(commands=['site', 'website'])
def site():
    webbrowser.open('https://github.com/fpmitucha/ChatGPT-API-bot')


# обрабатываем текст, который поступает от пользователя
# не нужно писать это в начале кода, иначе метод будет срабатывать каждый раз и код ниже будет недостижимым
@bot.message_handler()
def test(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.last_name} {message.from_user.first_name}.')
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, message.from_user.id)
    # рассмотрим метод, который позволяет "отвечать" на сообщение пользователя с помощью метода reply_to
    elif message.text.lower() == 'как дела?':
        bot.reply_to(message, 'Норм, а у тя?')


# делаем, чтобы программа работа бесконечно, можем использовать функцию bot.infinity_polling()
bot.polling(non_stop=True)
