import telebot

# توکن ربات رو اینجا با کوتیشن قرار بده
TOKEN = '7637390285:AAHv_nWEZcvbZ9yTnQCklcpkTn8X-dFiN5o'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات فعال شد.")

# شروع polling برای دریافت پیام‌ها
bot.polling()
