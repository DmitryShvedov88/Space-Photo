import requests
from pathlib import Path


def download_image(name, photo_format, down_load_link, number):
    filename = f'{name}_{number}.{photo_format}'
    path = Path(f"images/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(down_load_link)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
