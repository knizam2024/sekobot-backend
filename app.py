from flask import Flask
import telegram_bot.bot  # triggers the bot to start in a thread

app = Flask(__name__)

@app.route('/')
def index():
    return "SekoBot is running!"
