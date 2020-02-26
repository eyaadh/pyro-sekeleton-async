import os
import logging
from pyro.bot import bot
from pyro.utils.helpers.cat import cat
from pyrogram import Message, Filters, Emoji, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    InputMediaAnimation


@bot.on_message(Filters.command("gif", prefixes=['.', '/', '!']))
async def cat_gif_handler(c: bot, m: Message):
    cat_gif_file = await cat().cat_gif()
    await m.reply_animation(
        animation=cat_gif_file,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{Emoji.CAT} New Cat Gif", callback_data="new_cat_gif_callback")]
            ]
        )
    )

    try:
        os.remove(cat_gif_file)
    except Exception as e:
        logging.error(str(e))


@bot.on_callback_query(Filters.callback_data("new_cat_gif_callback"))
async def new_cat_gif_callback_handler(c: bot, cb: CallbackQuery):
    await cb.answer()

    cat_gif_file = await cat().cat_gif()

    await c.edit_message_media(
        chat_id=cb.message.chat.id,
        message_id=cb.message.message_id,
        media=InputMediaAnimation(cat_gif_file),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{Emoji.CAT} New Cat Gif", callback_data="new_cat_gif_callback")]
            ]
        )
    )

    try:
        os.remove(cat_gif_file)
    except Exception as e:
        logging.error(str(e))
