import telebot

bot = telebot.TeleBot("ВАШ_ТОКЕН")

# Обработчик /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я echo bot. Напиши мне что-нибудь.")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

bot.polling()