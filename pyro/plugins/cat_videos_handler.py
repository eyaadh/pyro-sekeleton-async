from pyro.bot import bot
from pyro.utils.ytdl import yt_dl
from pyro.utils.helpers.cat import cat
from pyrogram import Message, Filters


@bot.on_message(Filters.command("breed", prefixes=['.', '/', '!']))
async def cat_breed_handler(c: bot, m: Message):
    ack = await m.reply_text(
        text="<code>Searching Youtube for videos...</code>",
        parse_mode="html"
    )
    cat_breed = await cat().random_cat_breed()
    search_term = f"cat 101 {cat_breed}"
    # youtube_result = await youtube().search_yt(search_term)
    await yt_dl().dl_initiator('W65lD8A_5Rk', m.chat.id, ack.message_id, c)
