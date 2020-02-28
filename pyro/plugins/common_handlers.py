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


@bot.on_message(Filters.command('help', prefixes=['.', '/', '!']))
async def help_command_handler(c: bot, m: Message):
    help_msg = f"{Emoji.TOOLBOX}<b>Bot Commands:</b>\n" \
               "/start - Just the basic start message \n" \
               "/cat - I will send you a random cat \n" \
               "/gif - I will send you a random cat animation \n" \
               "/facts - I will send you a random fact about cats \n" \
               "/video - I will search youtube and send you a random cat video" \
               "/says something - I will send a cat which has the text something \n" \
               "@Kittenzbot inline query - basically I with an inline query I do the same " \
               "as what cat says but inline \n\n" \
               f"{Emoji.MEMO}<b>Command Prefixes:</b> The bot will accept the prefixes '!', '.' and '/'\n\n" \
               f"{Emoji.CAT}<b>About the Project: </b> This project was built to demonstrate how we at @baivaru structures - " \
               "our async @pyrogram projects. I could have written a skeleton (directory structures, modules showing " \
               "where plugins are loaded from and etc) which you could simply clone and build upon. However, doing " \
               "that could have left you halfway through the whole purpose of “making it easier” and having a " \
               "skeleton. Therefore, the project is a fully functional bot that demonstrates most of the common " \
               "methods, functionalities that pyrogram offers you to start programing a simple telegram bot and " \
               "some clean practices that we at @baivaru follow which you could refer and imply with your projects.\n\n" \
               "<b>Source of the Project:</b> <a href='https://github.com/eyaadh/pyro-sekeleton-async.git'>Github</a>"

    await m.reply_text(
        text=help_msg,
        parse_mode='html',
        disable_web_page_preview=True
    )

