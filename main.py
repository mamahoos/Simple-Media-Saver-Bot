from pyrogram import Client, filters, types
from utils import random_string, raw_link

media    = {}
bot      = Client('bot_session')
with bot : bot_username = bot.me.username
raw_link = raw_link.format(bot_username)


@bot.on_message(filters.private & filters.text)
async def _(_, message: types.Message):
    if len(message.text.split()) == 2 and message.text.split()[0] == '/start':
        key = message.text.split()[1]
        if key in media:
            file = media[key]
            await bot.copy_message(message.from_user.id, file['userid'], file['message_id'])


@bot.on_message(filters.private & filters.media)
async def _(_, message: types.Message):
    key = random_string(10)
    userid = message.from_user.id
    message_id = message.id

    media[key] = {'userid': userid, 'message_id': message_id}
    link = raw_link + key
    await message.reply(link)


bot.run()
