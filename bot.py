import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    "Maintenance-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

updatesc = os.environ["UPDATES_CHANNEL"]
supportc = os.environ["SUPPORT_CHAT"]

BOT_TEXT = """
Hai {} , This Bot Is Under Maintenance.

You Can't Use This Bot Right Now.You Will Get a Message On This Bot's Channel If This Bot Is Ready To Work.
"""

BOT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Channel", url=f"https://telegram.me/{updatesc}"),
            InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}"),
        ]
    ]
)


@bot.on_message(filters.private & filters.text)
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(BOT_BUTTONS)
    await message.reply_photo("https://telegra.ph/file/60fdc9e6682702bf4b471.jpg", caption=BOT_TEXT.format(message.from_user.mention), reply_markup=reply_markup)

# You Can See That Who Is Started The Bot On Logs

logging.info("Started the bot.")
bot.run()
