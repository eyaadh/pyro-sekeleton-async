from pyro.bot import bot
from pyro.utils.helpers.cat import cat
from pyro.utils.helpers.youtube import youtube
from pyrogram import Message, Filters


@bot.on_message(Filters.command("breed", prefixes=['.', '/', '!']))
async def cat_breed_handler(c: bot, m: Message):
    ack = await m.reply_text(
        text="<code>Searching Youtube for videos...</code>",
        parse_mode="html"
    )
    cat_breed = await cat().random_cat_breed()
    search_term = f"cat 101 {cat_breed}"
    youtube_result = await youtube().search_yt(search_term)


