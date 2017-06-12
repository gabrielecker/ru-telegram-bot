from bot.settings import DEFAULT_COMMANDS, REDIS_HOST
from redis import StrictRedis

redis = StrictRedis(**REDIS_HOST)


def get_menu(message):
    command = message.split('@')[0]
    if command not in DEFAULT_COMMANDS:
        raise Exception('Invalid command {}'.format(command))
    return redis.get(command.replace('/', '')).decode(encoding='UTF-8')
