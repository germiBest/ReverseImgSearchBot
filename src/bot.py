import logging
import requests
import json
import os
import tgconfig as cfg
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def quer(update, link):
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"image_url":"' + link + '", "resized_images":"True"}'
    response = requests.post('http://localhost:5000/search', headers=headers, data=data)
    json_data = json.loads(response.text)
    update.message.reply_text('The best match is: ' + json_data["best_guess"].encode('ascii', 'ignore'))
    return json_data

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('This bot is a service for searching by image. To use it, send an image or forward a message with a picture.')

def imga(update, context):
    update.message.reply_text("Processing...")
    lnk = update.message['photo'][-1].get_file(10)['file_path']
    jsdt = quer(update, lnk)
    for x in jsdt["links"]:
        update.message.reply_text(x)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    print(" ____   ___  ____   ____  ")
    print("|  _ \ |_ _|/ ___| | __ ) ")
    print("| |_) | | | \___ \ |  _ \ ")
    print("|  _ <  | |  ___) || |_) |")
    print("|_| \_\|___||____/ |____/ ")
    separator = ""
    sizet = int(os.popen('stty size', 'r').read().split()[1])
    for x in range(sizet):
        separator += "="
    print(separator)

    """Start the bot."""

    updater = Updater(cfg.api_token, use_context=True)


    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.photo, imga))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
