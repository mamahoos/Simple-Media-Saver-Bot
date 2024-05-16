from pyrogram import Client, filters, types
from string import ascii_letters, digits
from random import choice


bot = Client('bot_session')


def random_string(length):
    return ''.join(
        choice(digits + ascii_letters) 
        for _ in range(length))


media = {}
raw_link = 't.me/ali_akbar69_bot?start='


@bot.on_message(filters.private & filters.text)
async def _(cli, message: types.Message):
    if message.text == '/start':
        print('siktir')

    elif len(message.text.split()) == 2 and message.text.split()[0] == '/start':
        key = message.text.split()[1]
        fileinfo = media[key]

        file = await bot.copy_message(message.from_user.id, fileinfo['userid'], fileinfo['message_id'])
        await message.reply('payam 30 sec dige delete mishe')
        await sleep(30)
        await file.delete()


@bot.on_message(filters.private & filters.media)
async def _(cli, message: types.Message):
    key = random_string(10)
    userid = message.from_user.id
    message_id = message.id

    media[key] = {'userid': userid, 'message_id': message_id}
    link = raw_link + key

    await message.reply(
        link
    )



bot.run()
