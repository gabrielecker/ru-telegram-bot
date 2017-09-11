"""
This module holds all the bot handlers as well as the main thread method
"""
import asyncio
from datetime import datetime
from bot.commands import Command
from bot.logger import LOGGER
from bot.settings import TOKEN, DEFAULT_COMMANDS
from crawler.db import get_daily_menu, get_weekly_menu
from pytz import timezone
from telepot import glance
from telepot.aio import Bot
from telepot.aio.helper import Answerer
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle
from telepot.namedtuple import InputTextMessageContent

BOT = Bot(TOKEN)
ANSWERER = Answerer(BOT)


async def on_message(msg):
    """
    This function is responsible for handling all the plain text messages
    sent directly to the bot
    It returns None if the command does not exist or sends the corresponding
    string returned in Command class to the chat

    :type msg: string
    :param day: The message sent through chat
    """
    content_type, chat_type, chat_id = glance(msg)
    command = msg.get('text').split('@')[0].replace('/', '') or None

    if content_type != 'text' or command not in DEFAULT_COMMANDS:
        return None

    LOGGER.info('Message sent: %s - %s - %s',
                msg.get('text'), chat_id, chat_type)
    await BOT.sendMessage(chat_id, getattr(Command, command)())


def on_inline_query(msg):
    """
    This function is responsible for handling the inline queries
    which return the menus and are basically the core of the bot

    :type msg: string
    :param day: The message sent through chat
    """
    def compute():
        """
        This function is responsible from answering the inline query call
        """
        query_id, from_id, query_string = glance(msg, flavor='inline_query')
        LOGGER.info('Query string computed: %s - %s - %s',
                    query_id, from_id, query_string)
        day = datetime.now(timezone('America/Sao_Paulo')).weekday()
        articles = [
            InlineQueryResultArticle(
                id='hoje', title='Cardápio de hoje',
                thumb_url='https://i.imgur.com/jcggDJ9.jpg',
                input_message_content=InputTextMessageContent(
                    message_text=get_daily_menu(day),
                    parse_mode='Markdown'
                )
            ),
            InlineQueryResultArticle(
                id='semana', title='Cardápio da semana',
                thumb_url='https://i.imgur.com/RfS7QSj.jpg',
                input_message_content=InputTextMessageContent(
                    message_text=get_weekly_menu(),
                    parse_mode='Markdown'
                )
            )
        ]
        return articles

    ANSWERER.answer(msg, compute)


def on_chosen_inline_result(msg):
    """
    This function is responsible for logging the inline query results

    :type msg: string
    :param day: The message sent through chat
    """
    result_id, from_id, query_string = glance(msg,
                                              flavor='chosen_inline_result')
    LOGGER.info('Chosen Inline Result: %s, %s, %s',
                result_id, from_id, query_string)


def main():
    """
    This function is responsible for maintaining the main thread alive
    """
    handlers = {
        'chat': on_message,
        'inline_query': on_inline_query,
        'chosen_inline_result': on_chosen_inline_result
    }
    loop = asyncio.get_event_loop()
    loop.create_task(MessageLoop(BOT, handlers).run_forever())
    LOGGER.info('Listening...')
    loop.run_forever()
