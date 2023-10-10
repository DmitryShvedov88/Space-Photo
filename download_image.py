import requests
from pathlib import Path


def download_image(typer, find_url, i):
    if typer == "EPIC":
        photo_format = "png"
    else:
        photo_format = "jpeg"

    filename = f'{typer}_{i}.{photo_format}'
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(find_url)
        with open(path, 'wb') as file:
            file.write(response.content)
    except requests.HTTPError:
        print("Вы ввели неправильную ссылку")
