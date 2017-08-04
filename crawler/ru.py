import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bot.logger import logger
from bot.settings import RU_URL
from bs4 import BeautifulSoup
from crawler.db import redis


sched = BlockingScheduler()


def highlight(text):
    return '*{}*'.format(text)


def beautify(menu):
    beautified = []
    for item in menu:
        beautified.append(item.get_text().strip())

    beautified[2] = highlight(beautified[2])
    return beautified


def format_menu(index, day, items):
    menu = beautify(items[(index * 6):(index * 6 + 6)])
    daily_menu = '{} - {}'.format(
        highlight(day.get_text().capitalize()),
        ', '.join([item for item in menu])
    )
    return daily_menu


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def get_menu():
    page = requests.get(RU_URL)
    if page.status_code != 200:
        logger.warning('RU page was unavailable for some unknown reason')
        return None

    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all('td', {'align': 'center'})
    redis.flushdb()

    for index in range(5):
        week_day = soup.find_all('tr')[index + 1].find('td')
        print(index, format_menu(index, week_day, items))
        # redis.set(index, format_menu(index, week_day, items))
