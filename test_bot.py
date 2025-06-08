import telebot

TOKEN = "7637390285:AAHv_nWEZcvbZ9yTnQCklcpkTn8X-dFiN5o"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! بات من آماده است.")

bot.polling()
