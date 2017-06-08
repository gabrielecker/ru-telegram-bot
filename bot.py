import os
import asyncio
from functions import Crawler
from telepot import glance
from telepot.aio import Bot
from telepot.aio.loop import MessageLoop


TOKEN = os.environ['TELEGRAM_TOKEN']
API_URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
crawler = Crawler('http://ru.ufsc.br/ru/')
bot = Bot(TOKEN)


async def handle(msg):
    content_type, chat_type, chat_id = glance(msg)

    if content_type != 'text':
        return

    menu_items = crawler.get_menu(msg['text'])

    if menu_items:
        await bot.sendMessage(chat_id, 'Cardápio: {}.'.format(menu_items),
                              parse_mode='Markdown')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(MessageLoop(bot, handle).run_forever())
    print('Listening...')
    loop.run_forever()
