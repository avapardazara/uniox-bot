import telebot
import os
from telebot import types
from flask import Flask
from threading import Thread

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 102979428  # ← آیدی عددی خودت رو اینجا وارد کن

bot = telebot.TeleBot(BOT_TOKEN)

# ================= پیام خوش‌آمد و منو =================
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📚 سرفصل‌های دوره", "📍 محل برگزاری")
    markup.row("📝 ثبت‌نام در دوره", "📎 منابع دوره")
    markup.row("📩 ارتباط با پشتیبان", "📖 درباره دوره")
    bot.send_message(
        message.chat.id,
        "سلام! به ربات دوره Uniox خوش اومدی 👋\nیکی از گزینه‌های زیر رو انتخاب کن:",
        reply_markup=markup
    )

# ================= سرفصل‌ها =================
@bot.message_handler(func=lambda msg: msg.text == "📚 سرفصل‌های دوره")
def show_topics(message):
    text = """📚 سرفصل‌های دوره Uniox:

🟢 فرانت‌اند:
- سطح ۱: HTML, CSS, Flexbox
- سطح ۲: JavaScript, DOM, LocalStorage
- سطح ۳: Vue.js, Vue Router, Nuxt.js

🔵 بک‌اند (PHP):
- سطح ۱: مبانی PHP، فرم‌ها و GET/POST
- سطح ۲: پایگاه‌داده MySQL و عملیات CRUD
- سطح ۳: ساخت API، احراز هویت، اتصال به Vue
"""
    bot.send_message(message.chat.id, text)

# ================= آدرس =================
@bot.message_handler(func=lambda msg: msg.text == "📍 محل برگزاری")
def show_address(message):
    bot.send_message(
        message.chat.id,
        "📍 آدرس محل برگزاری:\nکرمان - بلوار جمهوری اسلامی - خیابان صادقیه - بین کوچه ۱ و ۳ - کارخانه نوآوری کرمان - شتابدهنده آوینوکس"
    )

# ================= منابع دوره =================
@bot.message_handler(func=lambda msg: msg.text == "📎 منابع دوره")
def show_resources(message):
    bot.send_message(
        message.chat.id,
        "📎 لینک منابع دوره:\n\n"
        "- فرانت‌اند: https://example.com/فرانت.html\n"
        "- بک‌اند: https://example.com/بک‌اند.html"
    )

# ================= ثبت‌نام =================
@bot.message_handler(func=lambda msg: msg.text == "📝 ثبت‌نام در دوره")
def show_signup(message):
    bot.send_message(
        message.chat.id,
        "برای ثبت‌نام در دوره Uniox روی لینک زیر کلیک کنید:\n\n"
        "📝 https://avinox.ir/events/یونی‌اکس-ویژه-برنامه-نویسان"
    )

# ================= پشتیبانی =================
@bot.message_handler(func=lambda msg: msg.text == "📩 ارتباط با پشتیبان")
def request_support(message):
    msg = bot.send_message(message.chat.id, "✍️ لطفاً پیام خود را برای پشتیبانی بنویس:")
    bot.register_next_step_handler(msg, forward_to_admin)

def forward_to_admin(message):
    user = f"{message.from_user.first_name} ({message.from_user.id})"
    text = f"📩 پیام از {user}:\n\n{message.text}"
    bot.send_message(ADMIN_ID, text)
    bot.send_message(message.chat.id, "✅ پیام شما به پشتیبانی ارسال شد.")

# ================= درباره دوره =================
@bot.message_handler(func=lambda msg: msg.text == "📖 درباره دوره")
def about_course(message):
    text = """📖 درباره دوره Uniox:

این دوره یک مسیر آموزشی ۳ سطحی برای یادگیری کامل توسعه وب است؛ از مبانی HTML و CSS تا Vue.js و ساخت API با PHP.

ویژگی‌ها:
- آموزش حضوری پروژه‌محور
- ارائه گواهی پایان‌دوره و کارآموزی
- امکان معرفی به بازار کار
- پشتیبانی مستمر و تیم مربیان

مکان برگزاری: کارخانه نوآوری کرمان – آوینوکس
"""
    bot.send_message(message.chat.id, text)

# ================= Flask server برای UptimeRobot =================
flask_app = Flask('')

@flask_app.route('/')
def home():
    return "✅ ربات Uniox در حال اجراست."

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

# ================= اجرای همزمان ربات و Flask =================
def run_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    Thread(target=run_bot).start()
    Thread(target=run_flask).start()
