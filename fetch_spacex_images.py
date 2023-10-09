# this script download photo
import requests
from pathlib import Path


def fetch_spacex_images(find_url, i):
    filename = f'space_{i}.jpeg'
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(find_url)
        print("response.status_code:", response.status_code)
        print("-------")
        with open(path, 'wb') as file:
            file.write(response.content)
    except:
        print("error")
