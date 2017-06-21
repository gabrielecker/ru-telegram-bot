from bot.settings import REDIS_URL
from redis import StrictRedis

redis = StrictRedis(*REDIS_URL)


def get_daily_menu(day):
    if day < 5:
        return redis.get(day).decode(encoding='UTF-8')
    else:
        return 'Cardápio indisponível'


def get_weekly_menu():
    weekly_menu = ''
    for day in range(0, 5):
        weekly_menu += '\n{}\n'.format(get_daily_menu(day))
    return weekly_menu
