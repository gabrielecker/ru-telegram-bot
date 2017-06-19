from bot import commands
from bot.logger import logger
from bot.settings import TOKEN, DEFAULT_COMMANDS
from crawler.db import get_menu
from telepot import glance
from telepot.aio import Bot
from telepot.aio.helper import Answerer
from telepot.namedtuple import InlineQueryResultArticle
from telepot.namedtuple import InputTextMessageContent

bot = Bot(TOKEN)
answerer = Answerer(bot)


async def on_message(msg):
    content_type, chat_type, chat_id = glance(msg)
    command = msg.get('text').split('@')[0].replace('/', '')
    logger.info('message sent: %s', msg.get('text'))

    if content_type != 'text' or command not in DEFAULT_COMMANDS:
        return None

    await bot.sendMessage(chat_id, getattr(commands, command)())


def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = glance(msg, flavor='inline_query')
        articles = [
            InlineQueryResultArticle(
                id='hoje', title='Cardápio de hoje',
                input_message_content=InputTextMessageContent(
                    message_text=get_menu('hoje'),
                    parse_mode='Markdown'
                )
            ),
            InlineQueryResultArticle(
                id='semana', title='Cardápio da semana',
                input_message_content=InputTextMessageContent(
                    message_text=get_menu('semana'),
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
