from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, OWNER_ID

bot = Client("bannerwebbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply(
        "Click below to open banner website:",
        reply_markup={
            "inline_keyboard": [[
                {"text": "Open Banner", "url": "https://hi-2bgf.onrender.com"}
            ]]
        }
    )

bot.run()
