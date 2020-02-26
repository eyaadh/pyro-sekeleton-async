import os
import logging
from pyro.bot import bot
from pyrogram import Message, Filters
from pyro.utils.helpers.cat import cat


@bot.on_message(Filters.command("says", prefixes=['.', '/', '!']))
async def cat_says_handler(c: bot, m: Message):
    if len(m.text.split(" ", 1)) > 1:
        text = m.text.split(" ", 1)[1]
    else:
        text = "hello"
    cat_says_file = await cat().cat_says(text)

    await m.reply_photo(cat_says_file)

    try:
        os.remove(cat_says_file)
    except Exception as e:
        logging.error(str(e))
