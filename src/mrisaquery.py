from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
def quer(update, link):
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"image_url":"' + link + '", "resized_images":"True"}'
    response = requests.post('http://localhost:5000/search', headers=headers, data=data)
    json_data = json.loads(response.text)
    update.message.reply_text('The best match is: ' + json_data["best_guess"].encode('ascii', 'ignore'))
    for x in json_data["links"]:
        update.message.reply_text(x)

