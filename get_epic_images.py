import os
import requests
from write_in_file import save_image


def get_epic(api_key):
    folder = 'EPIC'
    os.makedirs(folder, exist_ok=True)

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(epic_url, headers=headers)
    response.raise_for_status()
    photos = response.json()

    for index, photo in enumerate(photos, start=1):
        date_str = photo['date']
        split_date = date_str.split(' ')[0]
        year, month, day = split_date.split('-')
        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{photo["image"]}.png'
        save_image(image_url, folder, f'apod{index}', index, headers)


