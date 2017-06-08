import os


TOKEN = os.environ['TELEGRAM_TOKEN']
API_URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
RU_URL = 'http://ru.ufsc.br/ru/'
LOG_FORMAT = '%(asctime)s @%(username)-s %(message)s'
