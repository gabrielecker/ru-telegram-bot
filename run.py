#!/usr/bin/env python
from bot.handler import bot, handle, loop
from telepot.aio.loop import MessageLoop

if __name__ == '__main__':
    loop.create_task(MessageLoop(bot, handle).run_forever())
    print('Listening...')
    loop.run_forever()
