import asyncio
from bot import commands
from bot.logger import logger
from bot.settings import TOKEN, DEFAULT_COMMANDS
from crawler.db import get_daily_menu, get_weekly_menu
from datetime import datetime
from telepot import glance
from telepot.aio import Bot
from telepot.aio.helper import Answerer
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle
from telepot.namedtuple import InputTextMessageContent

bot = Bot(TOKEN)
answerer = Answerer(bot)


async def on_message(msg):
    content_type, chat_type, chat_id = glance(msg)
    command = msg.get('text').split('@')[0].replace('/', '')
    logger.info('message sent: %s - %s', msg.get('text'), chat_id)

    if content_type != 'text' or command not in DEFAULT_COMMANDS:
        return None

    await bot.sendMessage(chat_id, getattr(commands, command)())


def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = glance(msg, flavor='inline_query')
        day = datetime.today().weekday()
        articles = [
            InlineQueryResultArticle(
                id='hoje', title='Cardápio de hoje',
                input_message_content=InputTextMessageContent(
                    message_text=get_daily_menu(day),
                    parse_mode='Markdown'
                )
            ),
            InlineQueryResultArticle(
                id='semana', title='Cardápio da semana',
                input_message_content=InputTextMessageContent(
                    message_text=get_weekly_menu(),
                    parse_mode='Markdown'
                )
            )
        ]
        return articles

    answerer.answer(msg, compute)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = glance(msg,
                                              flavor='chosen_inline_result')
    logger.info('Chosen Inline Result: %s, %s, %s',
                result_id, from_id, query_string)


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(MessageLoop(bot, {
        'chat': on_message,
        'inline_query': on_inline_query,
        'chosen_inline_result': on_chosen_inline_result
    }).run_forever())
    print('Listening...')
    loop.run_forever()
