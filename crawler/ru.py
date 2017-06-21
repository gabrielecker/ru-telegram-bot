import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bot.settings import RU_URL
from bs4 import BeautifulSoup
from crawler.db import redis


sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=8)
def get_menu():
    soup = BeautifulSoup(requests.get(RU_URL).content, 'html.parser')

    for index, item in enumerate(soup.find_all('tr')[1:6]):
        week_day, daily_menu = item.find('td'), item.find_all('td')[1:]
        daily_menu[2].string = '*{}*'.format(daily_menu[2].string.strip())
        daily_menu = '*{}* - {}'.format(
            week_day.get_text().capitalize(),
            ', '.join([item.get_text().strip() for item in daily_menu])
        )
        redis.set(index, daily_menu)
