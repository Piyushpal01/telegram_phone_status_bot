import os
from dotenv import load_dotenv
import csv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# load token from enviornment variable
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Load dataset
def load_data(file_name):
    data = {}
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row["phone_number"]] = row["status"]
    return data

dataset = load_data("phone_dataset_100k.csv")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a phone number to check status.")

# Message handler
async def check_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()

    if user_input in dataset:
        await update.message.reply_text(f"Status: {dataset[user_input]}")
    else:
        await update.message.reply_text("Not Found")

# Main app
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_number))

print("Bot running...")
app.run_polling()
