from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import threading
import os

ALLOWED_GROUPS = [-38813096]  # Replace with real group chat IDs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id not in ALLOWED_GROUPS:
        await update.message.reply_text("🚫 This bot is not allowed in this group.")
        return

    keyboard = [
        [InlineKeyboardButton("📝 Submit Absence", web_app=WebAppInfo(url="https://sekobot-git-main-knizams-projects.vercel.app/?type=absence"))],
        [InlineKeyboardButton("🎉 Event Registration", web_app=WebAppInfo(url="https://sekobot-git-main-knizams-projects.vercel.app/?type=event"))],
        [InlineKeyboardButton("📚 Relief Request", web_app=WebAppInfo(url="https://sekobot-git-main-knizams-projects.vercel.app/?type=relief"))],
        [InlineKeyboardButton("🤝 Join Club", web_app=WebAppInfo(url="https://sekobot-git-main-knizams-projects.vercel.app/?type=club"))],
        [InlineKeyboardButton("🧩 Custom Form", web_app=WebAppInfo(url="https://sekobot-git-main-knizams-projects.vercel.app/?type=custom"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📌 Please choose an action:", reply_markup=reply_markup)

def main():
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# Background thread to run bot
bot_thread = threading.Thread(target=run_bot)
bot_thread.start()


if __name__ == "__main__":
    main()
