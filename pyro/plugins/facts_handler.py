from pyro.bot import bot
from pyro.utils.helpers.cat import cat
from pyrogram import Message, Filters, Emoji, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@bot.on_message(Filters.command("facts", prefixes=['.', '/', '!']))
async def cat_facts_handler(c: bot, m: Message):
    fact = await cat().cat_facts()
    await m.reply_text(
        text=fact,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{Emoji.BOOKS} New Fact", callback_data="new_facts")]
            ]
        )
    )


@bot.on_callback_query(Filters.callback_data("new_facts"))
async def new_facts_callback_handler(c: bot, cb: CallbackQuery):
    await cb.answer()
    fact = await cat().cat_facts()
    await c.edit_message_text(
        chat_id=cb.message.chat.id,
        message_id=cb.message.message_id,
        text=fact,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{Emoji.BOOKS} New Fact", callback_data="new_facts")]
            ]
        )
    )
