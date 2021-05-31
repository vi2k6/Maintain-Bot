import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Maintenance Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

updatesc = os.environ["UPDATES_CHANNEL"],
supportc = os.environ["SUPPORT_CHAT"]

BOT_TEXT = """
Hai {} , This Bot Is Under Maintenance.

You Can't Use This Bot Right Now.You Will Get a Message On This Bot's Channel If This Bot Is Ready To Work.To Know More Contact Support Group:)

ℹ️ Maintenance Bot.
"""

BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Channel", url=f"https://telegram.me/{updatesc}"),
        InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}")
        ]]
    )
                
@Bot.on_message(filters.private & filters.text)
async def start(bot, update):
    text = BOT_TEXT.format(update.from_user.mention)
    reply_markup = BOT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


Bot.run()
