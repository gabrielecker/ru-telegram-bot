#!/usr/bin/env python
import asyncio
from bot.handler import bot, on_message, on_inline_query, on_chosen_inline_result
from telepot.aio.loop import MessageLoop

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(MessageLoop(bot, {
        'chat': on_message,
        'inline_query': on_inline_query,
        'chosen_inline_result': on_chosen_inline_result
    }).run_forever())
    print('Listening...')
    loop.run_forever()
