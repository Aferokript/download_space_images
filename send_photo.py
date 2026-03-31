import telegram
import os
import time


def send_photo(bot_token, chat_id, interval):
    bot = telegram.Bot(token=bot_token)
    timer = interval * 60 * 60
    while True:
        folder = 'APOD'
        files = os.listdir(folder)
        for file in files:
            photo_path = os.path.join(folder, file)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)
                time.sleep(timer)

