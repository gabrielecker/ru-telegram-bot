"""
This module holds the logger configs within its main instance
"""
import logging
from bot.settings import LOG_FORMAT, LOG_LEVEL


logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
LOGGER = logging.getLogger('TelegramBot')
