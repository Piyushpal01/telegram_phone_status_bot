# Telegram Phone Status Bot

## Description
This is a Telegram bot that checks whether a phone number is Active or Inactive using a CSV dataset of 100,000 records.

## Features
- Fast O(1) lookup using dictionary
- Handles 100k dataset
- Returns Active / Inactive / Not Found

## Tech Stack
- Python 3.10+
- Flask
- python-telegram-bot (v20+ async)
- Gunicorn (Production WSGI server)
- CSV dataset

## Local Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt
3. Create `.env` File (in root folder)
3. Set environment variable:
   BOT_TOKEN=your_token_here
4. For Local Testing (Polling Mode), Temporarily update code of `bot_file.py` with:

```python
if __name__ == "__main__":
    telegram_app.run_polling()
```
6. Run:
   python bot.py
