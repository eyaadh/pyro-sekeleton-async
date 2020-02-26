from pyro.bot import bot
from pyrogram import Message, Filters, Emoji


@bot.on_message(Filters.command('start', prefixes=['.', '/', '!']))
async def start_command_handler(c: bot, m: Message):
    await m.reply_text(
        text=f"{Emoji.CAT_FACE_WITH_WRY_SMILE} Hello its nice to meet you, I am KittenZ. \n"
             f"A project that has been built to demonstrate how @baivaru structures their @pyrogram projects. "
             f"The source for this project is available "
             f"on <a href='https://github.com/eyaadh/pyro-sekeleton-async.git'>github</a>",
        parse_mode="html"
    )
