# Telegram Phone Status Bot

## Description
This is a Telegram bot that checks whether a phone number is Active or Inactive using a CSV dataset of 100,000 records.

## Features
- Fast O(1) lookup using dictionary
- Handles 100k dataset
- Returns Active / Inactive / Not Found

## Tech Stack
- Python
- python-telegram-bot
- CSV

## Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt
3. Set environment variable:
   BOT_TOKEN=your_token_here
4. Run:
   python bot.py
