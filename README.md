# ReverseImgSearchBot

---

RISB (**R**everse **I**mage **S**earch **B**ot) is a Telegram bot based on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and [MRISA](https://github.com/vivithemage/mrisa) which takes an image, does a reverse Google image search, and returns the best match and links to sites with this image.

## Usage
Install the necessary dependencies:

```shell
pip install -r requirments.txt
```

Setup your Telegram Bot API Token from [@BotFather](https://t.me/BotFather) in the file tgconfig.py:
```python
api_token="<your_api_token>"
```

Start the server with:

```shell
python mrisa/src/server.py
```

Or in the background

```shell
python mrisa/src/server.py &
```

And start the bot:
```shell
python ./src/bot.py
```

