from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests
import os

TOKEN = os.getenv("8233139162:AAFEoWSCB3vN5pWEV7dIX8IzfwiU5qVrIoM")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("⬇️ Download started...")

    try:
        r = requests.get(url, stream=True, timeout=15)
        filename = url.split("/")[-1] or "file.bin"

        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        await update.message.reply_text(f"✅ Download completed: {filename}")

    except Exception as e:
        await update.message.reply_text("❌ Download failed")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

app.run_polling()
