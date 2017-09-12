from bot.settings import TOKEN
from decouple import config
from telepot import Bot


def test_token():
    bot = Bot(TOKEN)
    assert bot.getMe().get('is_bot') is True


def test_message():
    bot = Bot(TOKEN)
    chat_id = config('CHAT_ID', cast=int)
    message = bot.sendMessage(chat_id, 'Testing new release...')
    assert message.get('message_id') is not None
