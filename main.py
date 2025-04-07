import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7645007167:AAEMhmRo1LEmEJp6BJt_tO6-9hKj5yPlVy8'
bot = telebot.TeleBot(TOKEN)

def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("ĐĂNG KÝ +888K", url="https://nh88trangchu.com")
    markup.add(button)
    bot.send_message(message.chat.id, "🎉 Nhấn vào nút bên dưới để nhận ngay +888K!", reply_markup=markup)

if __name__ == '__main__':
    print("Bot NH88 đang chạy...")
    bot.polling(non_stop=True)
