import logging
import os
import tgconfig as cfg
import re
import instagrab
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import telegram
import mrisaquery as mrisa

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def urlparse(update, context):
    parsee = re.search("(?P<url>https?://[^\s]+)", update.message.text.encode('ascii', 'ignore'))
    if parsee is not None:
        lst = instagrab.geturls(parsee.group("url"))
        if not lst == -1:
            if isinstance(lst, str):
                mrisa.quer(update, lst)
            else:
                mrisa.quer(update, lst[0])
        else:
            mrisa.quer(update, parsee.group("url"))

def start(update, context):
    update.message.reply_text('This bot is a service for searching by image. To use it, send an image or forward a message with a picture.')

def imga(update, context):
    update.message.reply_text("Processing...")
    lnk = update.message['photo'][-1].get_file(10)['file_path']
    jsdt = mrisa.quer(update, lnk)
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
    dp.add_handler(MessageHandler(Filters.text, urlparse))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
