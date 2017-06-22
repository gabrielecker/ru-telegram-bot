import logging
from bot.settings import LOG_FORMAT, LOG_LEVEL


logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger('TelegramBot')
