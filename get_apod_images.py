import os
import requests
from write_in_file import save_image
from dotenv import load_dotenv


def get_apod(api_key):
    folder = 'APOD'
    os.makedirs(folder, exist_ok=True)

    apod_url = 'https://api.nasa.gov/planetary/apod'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(apod_url, headers=headers)
    response.raise_for_status()
    photos = response.json()

    for index, photo in enumerate(photos, start=1):
        image_url = photo['url']
        save_image(image_url, folder, 'spacex_photo', index, headers)

def main():
    load_dotenv()
    get_apod()


if __name__ == '__main__':
    main()