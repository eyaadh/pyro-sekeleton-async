import os
from pathlib import Path
from pyro.utils import load_bot_configuration


class Common:
    def __init__(self):
        self.bot_config = load_bot_configuration()
        self.bot_config_file = Path("pyro/working_dir/config.ini")
        self.bot_working_dir = Path("pyro/working_dir/")
        self.session = self.bot_config.get("bot-configuration", "session_name")
        self.bot_api_key = self.bot_config.get("bot-configuration", "api_key")
        self.bot_workers = int(self.bot_config.get("bot-configuration", "workers"))
        self.tmp_dir = Path(self.bot_config.get("bot-configuration", "tmp_dir"))
        self.dustbin = int(self.bot_config.get("bot-configuration", "dustbin"))
        self.log_dir = self.bot_config.get("logging-configuration", "logging_dir")
        self.log_file = Path(f"{self.log_dir}/log.log")

    def init(self):
        """
            use of this def is to create the temp directories and get the bot ready for its session.
        """
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)


botCommon = Common()
