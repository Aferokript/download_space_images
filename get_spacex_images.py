import requests
import os
from write_in_file import save_image



def get_spacex(id='latest'):
    folder = 'spacex_photo'
    os.makedirs(folder, exist_ok=True)

    url = f'https://api.spacexdata.com/v5/launches/{id}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    spacex_photo = response.json()
    photos = spacex_photo['links']['flickr']['original']

    for index, photo in enumerate(photos, start=1):
        image = requests.get(photo, headers=headers)
        save_image(image, folder, f'spacex{index}', index, headers)


