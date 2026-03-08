import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# --- কনফিগারেশন ---
API_ID = 37538086  # আপনার আইডি বসান
API_HASH = "00d74cf414d526e9f2dc0adbb56566b0"
BOT_TOKEN = "8700514486:AAE3kNxODujV3Z-w-mdGn9UaUwDrHXVIvxU"

# --- Flask সার্ভার (বটকে জাগিয়ে রাখার জন্য) ---
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# --- বটের মূল কোড ---
app = Client("VIP_Creator_Bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("✨ VIP Auto Bot Creator চালু হয়েছে!")

# --- বট স্টার্ট করার ফাংশন ---
if __name__ == "__main__":
    # আগে Flask সার্ভার চালু হবে
    keep_alive()
    # তারপর টেলিগ্রাম বট চালু হবে
    print("Bot starting...")
    app.run()
