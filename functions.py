import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Crawler:

    def __init__(self, url):
        self.soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        self.commands = {
            '/hoje': self._get_daily_menu,
            '/semana': self._get_weekly_menu
        }

    def _get_daily_menu(self):
        today = datetime.today().weekday() + 1
        daily_menu = self.soup.find_all('tr')[today].find_all('td')[1:]
        return ', '.join([item.get_text() for item in daily_menu])

    def _get_weekly_menu(self):
        weekly_menu = ''
        for day in self.soup.find_all('tr')[1:6]:
            daily_menu, day = day.find_all('td')[1:], day.find('td')
            weekly_menu += '\n\n*%s* - %s' % (
                day.get_text(),
                ', '.join([item.get_text() for item in daily_menu])
            )
        return weekly_menu

    def get_menu(self, message):
        command = message.split('@')[0]
        if command not in self.commands:
            return None
        return self.commands[command]()
