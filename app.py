from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import telegram_bot.bot # triggers the bot to start in a thread

app = Flask(__name__)

@app.route('/')
def index():
    return "SekoBot is running!"


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
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# Background thread to run bot
if __name__ == "__main__":
    main()

    
