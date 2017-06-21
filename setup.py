#!/usr/bin/env python
from codecs import open
from os import path
from setuptools import setup, find_packages

root = path.abspath(path.dirname(__file__))

with open(path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = ['aiohttp', 'APScheduler', 'async-timeout', 'beautifulsoup4',
                'certifi', 'idna', 'chardet', 'multidict', 'python-decouple',
                'pytz', 'redis', 'requests', 'six', 'telepot', 'tzlocal',
                'urllib3', 'yarl']

setup(
    name='RU Telegram Bot',
    version='1.0',
    description='UFSC Telegram Bot',
    long_description=long_description,
    author='Gabriel Ecker',
    author_email='gabriel.ecker@gmail.com',
    license='MIT',
    url='https://github.com/gabrielecker/ru-telegram-bot/',
    packages=find_packages(),
    scripts=['bot/bot.py', 'crawler/scheduler.py'],
    install_requires=requirements,
    extra_require={
        'dev': ['ipdb', 'ipython']
    }
)
