import threading
import time
from flask import Flask
from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, OWNER_ID

# ----- FLASK KEEPALIVE -----
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)


# ----- TELEGRAM BOT -----
bot = Client(
    "bannerweb",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply(
        "Click below to open website:",
        reply_markup={
            "inline_keyboard": [[
                {"text": "Open Banner", "url": "https://hi-2bgf.onrender.com"}
            ]]
        }
    )


def run_bot():
    bot.run()


# ----- MULTITHREAD START -----
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_bot).start()

    while True:
        time.sleep(1)
