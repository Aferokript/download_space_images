import telegram


def send_photo(bot_token, chat_id, photo_path):
    bot = telegram.Bot(token=bot_token)

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

