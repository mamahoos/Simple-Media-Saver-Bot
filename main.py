from config import filters, types, bot, bot_username
from utils import random_string, raw_link

media    = {}
raw_link = raw_link.format(bot_username)

@bot.on_message(filters.private & filters.command('start'))
async def _(_, message: types.Message):
    splited_text = message.text.split()
    if len(splited_text) == 2:
        key = splited_text[1]
        if key in media:
            file = media[key]
            await bot.copy_message(message.from_user.id, file['userid'], file['message_id'])

@bot.on_message(filters.private & filters.media)
async def _(_, message: types.Message):
    while (key := random_string()) in media:   pass
    userid = message.from_user.id
    message_id = message.id
    media[key] = {'userid': userid, 'message_id': message_id}
    link = raw_link + key
    await message.reply(link)

bot.run()
