import os
import telebot

# Uzimamo token iz Heroku Config Vars (TOKEN ili BOT_TOKEN)
TOKEN = (os.getenv("TOKEN") or os.getenv("BOT_TOKEN") or "").strip()

# Ako nema tokena u okruženju, možeš ovde privremeno uneti ručno
if not TOKEN:
    TOKEN = "OVDE_STAVI_TVOJ_TOKEN"  # <--- samo privremeno testiranje
    if not TOKEN:
        print("⚠️ Nema TOKEN ili BOT_TOKEN u Heroku Config Vars!")
        raise SystemExit(1)

# Kreiranje bota
bot = telebot.TeleBot(TOKEN)

# Komanda /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Kripto Bot je spreman!")

# Komanda za signal
@bot.message_handler(func=lambda message: True)
def send_signal(message):
    par = message.text.upper()
    bot.send_message(message.chat.id, f"📈 Signal primljen za: {par}")

print("✅ Bot je pokrenut...")
bot.polling()
