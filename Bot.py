import os, telebot
TOKEN = os.getenv("TOKEN")  # ne kucaj token u kod više
bot = telebot.TeleBot(TOKEN)
TOKEN = "8012141190:AAFFOB6s2pAv0EhYVjmdSOLdwsT6uUk8EEk"
bot = telebot.TeleBot(TOKEN)

# Komanda /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Kripto bot je povezan! Pošalji mi par za trgovanje.")

# Komanda za signal
@bot.message_handler(func=lambda message: True)
def send_signal(message):
    par = message.text.upper()
    bot.send_message(message.chat.id, f"📊 Signal za {par} će biti poslat kada bude ulaz!")

print("Bot je pokrenut...")
bot.polling()
