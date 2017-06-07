import os
import time
from functions import get_daily_menu
from telepot import Bot, glance
from telepot.loop import MessageLoop


TOKEN = os.environ['TELEGRAM_TOKEN']
API_URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
COMMANDS = {
    '/hoje': get_daily_menu,
    # ...
}
bot = Bot(TOKEN)


def handle(msg):
    content_type, chat_type, chat_id = glance(msg)

    if content_type != 'text':
        return

    command = msg['text'].split('@')[0]
    if command in COMMANDS:
        menu = COMMANDS[command]()
        bot.sendMessage(chat_id, 'Cardápio do dia:{}.'.format(menu))


if __name__ == '__main__':
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
