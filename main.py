import telebot
from telebot.types import MenuButtonWebApp, WebAppInfo

TOKEN = "7645007167:AAEMhmRo1LEmEJp6BJt_tO6-9hKj5yPlVy8"
bot = telebot.TeleBot(TOKEN)

def welcome(message):
    # Gửi tin nhắn khi user bắt đầu
    bot.send_message(message.chat.id, "🎁 Chào mừng bạn đến với NH88!\nNhấn nút bên dưới để nhận +888K.")

    bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="🎯 ĐĂNG KÝ +888K",
            web_app=WebAppInfo(url="https://nh88trangchu.com")
        )
    )

if __name__ == '__main__':
    print("🤖 Bot NH88 đang chạy...")
    bot.polling(non_stop=True)
