#!/usr/bin/env python
import asyncio
from bot.handler import bot, handle
from telepot.aio.loop import MessageLoop

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(MessageLoop(bot, handle).run_forever())
    print('Listening...')
    loop.run_forever()
