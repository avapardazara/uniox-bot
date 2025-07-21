import telebot
import os

API_TOKEN = os.environ.get("7361793911:AAH_A-BDHt3xSMdyIC4bMeTLQFDjDzANxdc")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام 👋 به ربات دوره Uniox خوش اومدی!\nبرای دیدن برنامه کلاس‌ها بنویس /schedule")

@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    schedule = """
📅 برنامه این هفته:

🟢 فرانت‌اند:
- دوشنبه ساعت ۱۰ تا ۱۲
- چهارشنبه ساعت ۱۰ تا ۱۲

🔵 بک‌اند:
- یکشنبه ساعت ۱۴ تا ۱۶
- سه‌شنبه ساعت ۱۴ تا ۱۶
"""
    bot.send_message(message.chat.id, schedule)

bot.polling()
