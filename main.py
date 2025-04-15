import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analyze import analyze_news

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات تحلیل من فعال است. برای دریافت تحلیل، /analyze را بزن.")

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = analyze_news()
    await update.message.reply_text(f"تحلیل خودکار:\n{result}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyze", analyze))
    app.run_polling()