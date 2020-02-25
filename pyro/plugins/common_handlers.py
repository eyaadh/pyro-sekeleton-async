from pyro.bot import bot
from pyrogram import Message, Filters, Emoji


@bot.on_message(Filters.command('start', prefixes=['.', '/', '!']))
async def start_command_handler(c: bot, m: Message):
    await m.reply_text(
        f"Yo this is just a our pyro-skeleton. {Emoji.MAN_SHRUGGING}"
    )
