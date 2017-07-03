import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bot.logger import logger
from bot.settings import RU_URL
from bs4 import BeautifulSoup
from crawler.db import redis


sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def get_menu():
    page = requests.get(RU_URL)
    if page.status_code != 200:
        logger.warning('RU page was unavailable for some unknown reason')
        return None

    soup = BeautifulSoup(page.content, 'html.parser')
    for index, item in enumerate(soup.find_all('tr')[1:6]):
        week_day, daily_menu = item.find('td'), item.find_all('td')[1:]
        daily_menu[2].string = '*{}*'.format(daily_menu[2].string.strip())
        daily_menu = '*{}* - {}'.format(
            week_day.get_text().capitalize(),
            ', '.join([item.get_text().strip() for item in daily_menu])
        )
        redis.set(index, daily_menu)
