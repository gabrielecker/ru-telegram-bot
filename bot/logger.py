import logging
from bot.settings import LOG_FORMAT


logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger('telegrambot')
