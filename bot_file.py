import os
import csv
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# Load token
TOKEN = os.getenv("BOT_TOKEN")
print(TOKEN)
app = Flask(__name__)

# Load csv data - fn will read the csv data and convert in dict
def load_data(file_name):
    data = {}
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row["phone_number"]] = row["status"]
    return data

# loading dataset
dataset = load_data("phone_dataset_100k.csv")

# TG Handlers
# TG start command - runs for /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send a phone number to check status.")

# number validation - runs when user send any message
async def check_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    # check if num exist in dataset
    if number in dataset:
        await update.message.reply_text(f'Status: {dataset[number]}')
    else:
        await update.message.reply_text("Not Found")

# creating tg application
telegram_app = ApplicationBuilder().token(TOKEN).build()

# adding Command and message handlers
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_number))

# Flask routes
@app.route("/webhook", methods=["POST"])
async def webhook():
    # whenver tg send post req it will be received here, we convert the json data into Update object, then process it using process dispatcher

    # ensure that tg app is initialized and running
    if not telegram_app.running:
        await telegram_app.initialize()
        await telegram_app.start()

    data = request.get_json()

    # converting json to tg update object
    update = Update.de_json(data, telegram_app.bot)

    # process update using telegram dispatcher
    await telegram_app.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

# start server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    # # run flask server
    app.run(host="0.0.0.0", port=port)

    # for locally testing
    # telegram_app.run_polling()