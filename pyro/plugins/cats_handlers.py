import os
import logging
import secrets
from pyro.bot import bot
from pyro.helpers.cat import cat
from pyrogram.client.ext import utils
from pyro.utils.common import botCommon
from pyrogram.api import functions, types
from pyrogram.errors import QueryIdInvalid
from pyro.helpers.file_properties import CustomFileProperties
from pyrogram import Message, Filters, Emoji, InlineQuery, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    InputMediaPhoto, InputMediaAnimation


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


@bot.on_message(Filters.command("catsays", prefixes=['.', '/', '!']))
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


@bot.on_message(Filters.command("catgif", prefixes=['.', '/', '!']))
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


@bot.on_inline_query()
async def inline_handler(c: bot, q: InlineQuery):
    text = q.query
    text = text if text else "Hello"
    cat_says_photo = await cat().cat_says(text)

    cat_says_photo_uploaded = await c.send_photo(
        chat_id=botCommon.dustbin,
        photo=str(cat_says_photo)
    )

    try:
        os.remove(cat_says_photo)
    except Exception as e:
        logging.error(str(e))

    cat_says_file_properties = await CustomFileProperties().get_properties(
        client=c,
        m_message_id=cat_says_photo_uploaded.message_id,
        m_chat_id=cat_says_photo_uploaded.chat.id
    )

    try:
        await c.send(
            functions.messages.SetInlineBotResults(
                query_id=int(q.id),
                cache_time=0,
                results=[
                    types.InputBotInlineResultPhoto(
                        id=str(secrets.token_hex(4)),
                        type="photo",
                        photo=types.InputPhoto(
                            id=cat_says_file_properties.document_id,
                            access_hash=cat_says_file_properties.access_hash,
                            file_reference=utils.decode_file_ref(cat_says_file_properties.file_ref)
                        ),
                        send_message=types.InputBotInlineMessageMediaAuto(
                            message=q.query
                        )
                    )

                ]
            )
        )
    except QueryIdInvalid:
        pass
