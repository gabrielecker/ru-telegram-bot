from bot.settings import REDIS_URL
from redis import StrictRedis

redis = StrictRedis(*REDIS_URL)


def get_menu(command):
    return redis.get(command).decode(encoding='UTF-8')
