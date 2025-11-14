import os
import asyncio
from flask import Flask
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Import modules
from modules.ai_engine import ai_medical_response
from modules.drug_engine import get_drug_info
from modules.telemedicine_engine import telemedicine_triage


TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ ERROR: TOKEN not found!")
    raise SystemExit


# ---------- Commands ----------

async def start(update, context):
    await update.message.reply_text(
        "👋 مرحباً! أنا مساعد المستشفى الذكي.\n"
        "استخدم الأوامر التالية:\n\n"
        "🧠 /ai لتحليل الأعراض\n"
        "💊 /drug لمعلومات دوائية\n"
        "🩺 /tele للاستشارة الطبية عن بعد\n"
    )


async def ai_command(update, context):
    symptoms = " ".join(context.args)
    if not symptoms:
        await update.message.reply_text("🧠 أرجوك اكتب الأعراض بعد الأمر /ai")
        return

    reply = ai_medical_response(symptoms)
    await update.message.reply_text(reply)


async def drug_command(update, context):
    drug = " ".join(context.args)
    if not drug:
        await update.message.reply_text("💊 أرجوك اكتب اسم الدواء بعد /drug")
        return

    reply = get_drug_info(drug)
    await update.message.reply_text(reply)


async def tele_command(update, context):
    symptoms = " ".join(context.args)
    if not symptoms:
        await update.message.reply_text("🩺 أرجوك اكتب الأعراض بعد /tele")
        return

    reply = telemedicine_triage(symptoms)
    await update.message.reply_text(reply)


# ---------- Run Bot ----------

async def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ai", ai_command))
    app.add_handler(CommandHandler("drug", drug_command))
    app.add_handler(CommandHandler("tele", tele_command))

    print("🤖 Bot is running...")
    await app.run_polling()


# Flask for Replit Uptime
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running"


def run_web():
    flask_app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    import threading
    threading.Thread(target=run_web).start()
    asyncio.run(run_bot())
