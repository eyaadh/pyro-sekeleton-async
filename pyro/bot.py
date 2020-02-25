import logging
from pyrogram import Client
from pyrogram import __version__
from pyrogram.api.all import layer
from pyro.utils.common import botCommon


class bot(Client):
    def __init__(self):
        super().__init__(
            session_name=botCommon.session,
            bot_token=botCommon.bot_api_key,
            config_file=botCommon.bot_config_file,
            workdir=botCommon.bot_working_dir,
            workers=botCommon.bot_workers
        )

    async def start(self):
        await super().start()
        logging.info(f"{botCommon.session} initiated with Pyrogram v{__version__} "
                     f"(Layer {layer}) started. Hello World!")

    async def stop(self):
        await super().stop()
        logging.info(f"{botCommon.session} session Terminated!")
