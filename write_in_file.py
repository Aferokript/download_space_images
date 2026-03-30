import requests
import os


def save_image(image_url, folder, filename_prefix, index, headers):
    image = requests.get(image_url, headers=headers)
    image.raise_for_status()
    filename = os.path.join(folder, f'{filename_prefix}_{index}.jpg')
    with open(filename, 'wb') as file:
        file.write(image.content)

