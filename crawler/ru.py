"""
This module holds the functions to crawl and format stuff from the website
"""
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bot.logger import LOGGER
from bot.settings import RU_URL
from bs4 import BeautifulSoup
from crawler.db import REDIS


SCHED = BlockingScheduler()


def highlight(text):
    """
    This function takes a text and returns it in bold

    :type text: string
    :param text: The string to be highlighted
    """
    return '*{}*'.format(text)


def beautify(menu):
    """
    This function takes a text and returns an array with beautified items

    :type menu: string
    :param menu: The menu text to be beautified (e.g. removing whitespaces)
    """
    beautified = []
    for item in menu:
        beautified.append(item.get_text().strip())

    beautified[2] = highlight(beautified[2])
    return beautified


def format_menu(day, menu):
    """
    This function returns the menu formatted for easy human readability

    :type day: string
    :param day: The week day as a string to be inserted (e.g. segunda-feira)

    :type menu: array
    :param menu: The menu array to be inserted
    """
    formatted_menu = '{} - {}'.format(
        highlight(day.get_text().capitalize()),
        ', '.join([item for item in menu])
    )
    return formatted_menu


@SCHED.scheduled_job('cron', day_of_week='mon-fri', hour=11)
def get_menu():
    """
    This function is scheduled to run daily and save the menu information
    collected from the website on redis
    """
    page = requests.get(RU_URL)

    if page.status_code != 200:
        LOGGER.warning('RU page was unavailable for some unknown reason')
        return None

    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all('td', {'align': 'center'})
    REDIS.flushdb()

    for index in range(5):
        menu = beautify(items[(index * 6):(index * 6 + 6)])
        week_day = soup.find_all('tr')[index + 1].find('td')
        REDIS.set(index, format_menu(week_day, menu))
