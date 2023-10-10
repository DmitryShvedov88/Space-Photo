# this script download photo
import requests
from pathlib import Path


def fetch_nasa_epic(find_url, date):
    filename = f'epic_{date}.png'
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(find_url)
        with open(path, 'wb') as file:
            file.write(response.content)
    except requests.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")
