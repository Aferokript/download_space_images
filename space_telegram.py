import argparse
import os
from dotenv import load_dotenv
from get_epic_images import get_epic
from get_spacex_images import get_spacex
from get_apod_images import get_apod
from send_photo import send_photo


def main():
    load_dotenv()

    nasa_api_key = os.environ['NASA_API_KEY']
    telegram_token = os.environ['TELEGRAM_TOKEN']

    parser = argparse.ArgumentParser(description='Загрузка и отправка космических фото')
    parser.add_argument('--source', choices=['spacex', 'apod', 'epic'],
                        help='Источник изображений')
    parser.add_argument('--send', action='store_true',
                        help='Отправить фото в Telegram')
    parser.add_argument('--photo', default='path/to/photo.jpg',
                        help='Путь к фото для отправки')
    parser.add_argument('--chat_id', default='@your_channel',
                        help='ID чата Telegram')

    args = parser.parse_args()

    if args.source == 'spacex':
        get_spacex()
    elif args.source == 'apod':
        get_apod(nasa_api_key)
    elif args.source == 'epic':
        get_epic(nasa_api_key)

    if args.send:
        send_photo(
            bot_token=telegram_token,
            chat_id=args.chat_id,
            photo_path=args.photo
        )


if __name__ == '__main__':
    main()









































