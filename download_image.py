import requests
from pathlib import Path


def download_image(name, photo_format, find_url, i):
    filename = f'{name}_{i}.{photo_format}'
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(find_url)
        print("response.status_code", response.status_code)
        with open(path, 'wb') as file:
            file.write(response.content)
    except requests.HTTPError:
        print("Вы ввели неправильную ссылку")
