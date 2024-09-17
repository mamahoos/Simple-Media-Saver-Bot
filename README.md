# Simple Media Saver Bot

Simple-Media-Saver-Bot is a Telegram bot designed to allow users to store their media. Written using the Pyrogram library, it enables users to send media to the bot and receive a unique link to access their media.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/mamahoos/Simple-Media-Saver-Bot.git
```   

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```  

3. Create a `.env` file with the following variables:
```env
api_id=YOUR_API_ID
api_hash=YOUR_API_HASH
bot_token=YOUR_BOT_TOKEN
```   
You can obtain the `api_id` and `api_hash` from the [Telegram website](https://my.telegram.org/). Obtain the `bot_token` from the [BotFather](https://t.me/BotFather) bot on Telegram.

4. Run the bot:
```bash
python3 main.py
```   

## Usage

- Send any media file to the bot in a private chat to save it.
- The bot will generate a unique link for each saved media file.
- Use the generated link to retrieve the saved media file.

## Features

- Saves media files with unique keys.
- Retrieves saved media files using the generated links.

Feel free to contribute to this project and enhance its functionality!

## TODO
- [ ] Implement functionality to handle `media-groups`.
- [ ] Using databases.

---

For more information, visit the [Pyrogram documentation](https://docs.pyrogram.org/).
