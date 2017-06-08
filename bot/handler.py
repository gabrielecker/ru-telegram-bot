import asyncio
from bot.logger import logger
from bot.settings import RU_URL, TOKEN
from crawlers.ru import RUCrawler
from telepot import glance
from telepot.aio import Bot

crawler = RUCrawler(RU_URL)
bot = Bot(TOKEN)
loop = asyncio.get_event_loop()


async def handle(msg):
    content_type, chat_type, chat_id = glance(msg)
    info = {'username': msg.get('chat').get('username')}

    if content_type != 'text':
        return None

    try:
        menu_items = crawler.get_menu(msg.get('text'))
        logger.info('message sent: %s', msg.get('text'), extra=info)
        await bot.sendMessage(chat_id, '*Cardápio*: {}.'.format(menu_items),
                              parse_mode='Markdown')
    except Exception as e:
        logger.warning('message failed: %s', e, extra=info)
