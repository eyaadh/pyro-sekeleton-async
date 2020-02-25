import logging
from logging.handlers import TimedRotatingFileHandler
from pyro.utils.common import botCommon, Common

Common().init()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        TimedRotatingFileHandler(botCommon.log_file, when="midnight", encoding=None,
                                 delay=False, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger(__name__)