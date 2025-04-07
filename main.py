
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7645007167:AAEMhmRo1LEmEJp6BJt_tO6-9hKj5yPlVy8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🚀 Truy cập NH88", web_app={"url": "https://nh88trangchu.com"})
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎰 Chào mừng đến với NH88! Bấm nút bên dưới để mở mini app:",
        reply_markup=reply_markup
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
