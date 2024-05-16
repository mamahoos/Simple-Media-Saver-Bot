from os import getenv
__import__('dotenv').load_dotenv()


API_ID    = int(getenv('api_id'))
API_HASH  = getenv('api_hash')
BOT_TOKEN = getenv('bot_token')

from pyrogram import Client, types, filters

bot = Client(
    'bot_session',
    bot_token=BOT_TOKEN,
    api_hash=API_HASH,
    api_id=API_ID,
)

with bot:
    bot_username = bot.me.username