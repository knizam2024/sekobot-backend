from flask import Flask
import telegram_bot.bot # triggers the bot to start in a thread

app = Flask(__name__)

@app.route('/')
def index():
    return "SekoBot is running!"

async def get_chat_id(update, context):
    chat = update.effective_chat
    print(f"Group name: {chat.title}, ID: {chat.id}")

app = ApplicationBuilder().token("7887402540:AAFQkdijjgFu-II1Of_JZfN34XfxVhGQXB4").build()
app.add_handler(MessageHandler(filters.ALL, get_chat_id))
app.run_polling()
    
