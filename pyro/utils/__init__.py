import configparser
from pathlib import Path


def load_bot_configuration():
    config = configparser.ConfigParser()
    config.read(Path("pyro/working_dir/config.ini"))

    return config
