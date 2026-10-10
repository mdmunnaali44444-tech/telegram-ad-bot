TEXT & import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# এখানে তোমার BotFather থেকে পাওয়া Token বসাবে
BOT_TOKEN = 8855630337:AAE11zgym6upYZWZg6ry2hUmKgKQhq6bbro

# তোমার এডের চ্যানেল / গ্রুপ ID, যেখানে এড যাবে
# যেমন: -1001234567890
AD_CHANNEL_ID = "@bdearnig3090"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "হাই! আমি তোমার এড বট।\n\n"
        "কমান্ড:\n"
        "/ad - নতুন এড পোস্ট করতে\n"
        "যেকোনো মেসেজ পাঠালে আমি সেটা চ্যানেলে পোস্ট করে দেবো"
    )

async def ad_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # /ad এর পরের লেখাটাই এড হিসেবে যাবে
    ad_text = ' '.join(context.args)
    if not ad_text:
        await update.message.reply_text("এভাবে লিখো: /ad তোমার এডের লেখা")
        return
    
    # চ্যানেলে পোস্ট
    await context.bot.send_message(chat_id=AD_CHANNEL_ID, text=f"📢 নতুন এড:\n\n{ad_text}")
    await update.message.reply_text("✅ এড সফলভাবে চ্যানেলে পোস্ট হয়েছে!")

async def auto_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # তুমি বটকে যা পাঠাবে সেটাই এড হিসেবে চ্যানেলে চলে যাবে
    await context.bot.send_message(chat_id=AD_CHANNEL_ID, text=update.message.text)
    await update.message.reply_text("✅ পাঠানো হয়েছে")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ad", ad_command))
    app.add_handler(MessageHandler(filters..
