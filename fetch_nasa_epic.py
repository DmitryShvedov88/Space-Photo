#this script download photo
import requests
from pathlib import Path


def fetch_nasa_epic(find_url, i):
    print("find_url", find_url)
    filename = f'epic_{i}.png'
    print(filename)
#Создание папки, если ее не существует
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(find_url) #, params=payload
        #print("response.url:", response.url)
        print("response.status_code:", response.status_code)
        print("-------")
        with open(path, 'wb') as file:
            file.write(response.content)
    except:
        print("error")