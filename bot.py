import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
AD_CHANNEL_ID = "@bdearnig3090"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "হাই! আমি তোমার এড বট।\n\n"
        "কমান্ড:\n"
        "/ad - নতুন এড পোস্ট করতে\n"
        "যেকোনো মেসেজ পাঠালে আমি সেটা চ্যানেলে পাঠাবো"
    )

async def ad_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("তোমার এড টি পাঠাও, আমি চ্যানেলে পোস্ট করে দিচ্ছি।")

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.copy_message(
            chat_id=AD_CHANNEL_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
        await update.message.reply_text("✅ এড চ্যানেলে পোস্ট হয়েছে!")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ad", ad_command))
    app.add_handler(MessageHandler(filters.ALL, forward_to_channel))
    app.run_polling()

if __name__ == "__main__":
    main()
