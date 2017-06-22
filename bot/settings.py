import logging
from decouple import config

# Bot token obtained from BotFather and HTTP api for testing
TOKEN = config('TELEGRAM_TOKEN')
API_URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)

# Crawler URL
RU_URL = 'http://ru.ufsc.br/ru/'

# Logging settings
LOG_FORMAT = '%(asctime)s %(message)s'
LOG_LEVEL = logging.INFO

# Default bot chat commands
DEFAULT_COMMANDS = ['start', 'help', 'settings']

# Database url for the crawler and handlers
REDIS_URL = config('REDIS_URL').split(':')
