import date
import time
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Maintenance Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"],
        upchl = os.environ["UPDATES_CHANNEL"],
        suppchat = os.environ["SUPPORT_CHAT"]
)

START_TEXT = """
Hai {} , This Bot Is Under Maintenance.

You Can't Use This Bot Right Now.You Will Get a Message On This Bot's Channel If This Bot Is Ready To Work.To Know More Contact Support Group:)

ℹ️ Maintenance Bot.
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel') url='https://telegram.me/suppchat'),
        InlineKeyboardButton('Support') url='https://t.me/upchl')
        ]]
    )
                
@Bot.on_message(filters.private & filters.text)
async def text(bot,update):
    text = START_TEXT.format(update.from_user.mention)
    replay_markup = START_BUTTONS
    await update.replay_text(
        text=text,
        disable_web_page_preview=true,
        reply_markup=reply_markup
    )


Bot.run()
