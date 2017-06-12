import requests
from bot.db import redis
from bot.settings import RU_URL
from bs4 import BeautifulSoup
from datetime import datetime

soup = BeautifulSoup(requests.get(RU_URL).content, 'html.parser')


def get_daily_menu():
    today = datetime.today().weekday() + 1
    items = soup.find_all('tr')[today].find_all('td')[1:]
    daily_menu = ', '.join([item.get_text() for item in items])
    redis.set('hoje', daily_menu)


def get_weekly_meu():
    weekly_menu = ''
    for day in soup.find_all('tr')[1:6]:
        daily_menu, day = day.find_all('td')[1:], day.find('td')
        weekly_menu += '\n\n*{}* - {}'.format(
            day.get_text(),
            ', '.join([item.get_text() for item in daily_menu])
        )
    redis.set('semana', weekly_menu)


if __name__ == '__main__':
    get_daily_menu()
    get_weekly_meu()
