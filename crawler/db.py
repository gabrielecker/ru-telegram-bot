"""
This module holds the database calls which get sent by the handlers
"""
from bot.settings import REDIS_URL
from redis import StrictRedis

REDIS = StrictRedis(*REDIS_URL)


def get_daily_menu(day):
    """
    This function returns the daily menu based on 'day' parameter
    or None in case day is invalid

    :type day: int
    :param day: The integer representing week day (0-6)
    """
    if day < 5:
        return REDIS.get(day).decode(encoding='UTF-8')
    else:
        return 'Cardápio indisponível'


def get_weekly_menu():
    """
    This function runs through all available days (0-4) and returns
    all menus together by calling 'get_daily_menu' function multiple times
    """
    weekly_menu = ''
    for day in range(0, 5):
        weekly_menu += '\n{}\n'.format(get_daily_menu(day))
    return weekly_menu
