import os
import logging
import secrets
from pyro.bot import bot
from pyrogram import InlineQuery
from pyro.utils.helpers.cat import cat
from pyrogram.client.ext import utils
from pyro.utils.common import botCommon
from pyrogram.api import functions, types
from pyrogram.errors import QueryIdInvalid
from pyro.utils.helpers.file_properties import CustomFileProperties


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
