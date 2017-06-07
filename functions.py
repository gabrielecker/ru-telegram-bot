import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_daily_menu():
    soup = BeautifulSoup(
        requests.get('http://ru.ufsc.br/ru/').content,
        'html.parser'
    )
    today = datetime.today().weekday() + 1
    menu_items = soup.find_all('tr')[today].find_all('td')[1:]
    return ', '.join([item.get_text() for item in menu_items])
