import os


TOKEN = os.environ['TELEGRAM_TOKEN']
API_URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
RU_URL = 'http://ru.ufsc.br/ru/'
LOG_FORMAT = '%(asctime)s @%(username)-s %(message)s'
DEFAULT_COMMANDS = ['/hoje', '/semana']
REDIS_HOST = {
    'host': os.environ['REDIS_HOST'],
    'port': os.environ['REDIS_PORT'],
    'db': os.environ['REDIS_DB']
}
