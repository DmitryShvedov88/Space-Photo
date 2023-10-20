import requests
from pathlib import Path


def download_image(name, photo_format, down_load_link, i):
    filename = f'{name}_{i}.{photo_format}'
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(down_load_link)
        with open(path, 'wb') as file:
            file.write(response.content)
    except requests.HTTPError:
        print("Вы ввели неправильную ссылку")
