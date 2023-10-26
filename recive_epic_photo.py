import requests
import datetime
import argparse
import os
from dotenv import load_dotenv, find_dotenv
from download_image import download_image


def taker_epic_links(epic__number, payload) -> list:
    epic_link = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(epic_link, params=payload)
    response.raise_for_status()
    photos_informarion = response.json()
    for number in range(epic__number):
        name = photos_informarion[number]["image"]
        date = photos_informarion[number]["date"]
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png'
        photo_name = "EPIC"
        photo_format = "png"
        download_image(photo_name, photo_format, find_url, date)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    payload = {"api_key": os.getenv("NASA_TOKEN")}
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии с сайта NASA'
        )
    parser.add_argument('EPIC', help='Введите кол фотографий EPIC для скачивания', type=int, default=1)
    args = parser.parse_args()
    epic__number = args.EPIC
    try:
        taker_epic_links(epic__number, payload)
    except SyntaxError:
        print("<h1>SyntaxError: invalid syntax</h1>")
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")
    except NameError:
        print("По этой ссылке не фотом для скачивания")
