import os
import logging
from pyro.bot import bot
from pyro.utils.helpers.cat import cat
from pyrogram import Message, Filters, Emoji, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    InputMediaPhoto


@bot.on_message(Filters.command("cat", prefixes=['.', '/', '!']))
async def cat_handler(c: bot, m: Message):
    cat_file = await cat().random_cat()
    await m.reply_photo(
        photo=cat_file,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{Emoji.CAT_FACE} New Cat", callback_data="new_cat_callback")]
            ]
        )
    )

    try:
        os.remove(cat_file)
    except Exception as e:
        logging.error(str(e))


@bot.on_callback_query(Filters.callback_data("new_cat_callback"))
async def new_cat_callback_handler(c: bot, cb: CallbackQuery):
    await cb.answer()
    cat_file = await cat().random_cat()

    await c.edit_message_media(
        chat_id=cb.message.chat.id,
        message_id=cb.message.message_id,
        media=InputMediaPhoto(cat_file),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{Emoji.CAT_FACE} New Cat", callback_data="new_cat_callback")]
            ]
        )
    )

    try:
        os.remove(cat_file)
    except Exception as e:
        logging.error(str(e))
