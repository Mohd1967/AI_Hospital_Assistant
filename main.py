import os
import asyncio
from flask import Flask
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ ERROR: TOKEN not found!")
    raise SystemExit

async def start(update, context):
    await update.message.reply_text("👋 أهلاً دكتور محمد… البوت يعمل الآن بنجاح!")

async def reply(update, context):
    text = update.message.text
    await update.message.reply_text(f"📩 استلمت رسالتك: {text}")

async def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("🤖 Bot is running…")
    await app.run_polling()

# Flask server (for uptime)
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running"

def run_web():
    flask_app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_web).start()
    asyncio.run(run_bot())
