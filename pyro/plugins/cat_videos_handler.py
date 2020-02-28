from pyro.bot import bot
from pyro.utils.ytdl import yt_dl
from pyro.utils.helpers.cat import cat
from pyrogram import Message, Filters
from pyro.utils.helpers.youtube import youtube


@bot.on_message(Filters.command("video", prefixes=['.', '/', '!']))
async def cat_breed_handler(c: bot, m: Message):
    cat_breed = await cat().random_cat_breed()
    ack = await m.reply_text(
        text=f"<code>Searching Youtube for videos about {cat_breed} cats...</code>",
        parse_mode="html"
    )
    search_term = f"cat 101 {cat_breed}"
    youtube_result = await youtube().search_yt(search_term)
    await yt_dl().dl_initiator(youtube_result[0]['video_id'], m.chat.id, ack.message_id, c)
