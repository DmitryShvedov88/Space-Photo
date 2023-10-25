import requests
import datetime
import argparse
import os
from dotenv import load_dotenv, find_dotenv
from download_image import download_image
load_dotenv(find_dotenv())


def taker_epic_links(epic_link, payload, epic__number) -> list:
    response = requests.get(epic_link, params=payload)
    response.raise_for_status()
    texts = response.json()
    for number in range(epic__number):
        name = texts[number]["image"]
        date = texts[number]["date"]
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png'
        photo_name = "EPIC"
        photo_format = "png"
        download_image(photo_name, photo_format, find_url, date)


def conect_nasa_epic(epic__number, payload):
    epic_link = "https://api.nasa.gov/EPIC/api/natural/images"
    taker_epic_links(epic_link, payload, epic__number)


if __name__ == "__main__":
    payload = {"api_key": os.getenv("NASA_TOKEN")}
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('EPIC', help='Введите кол фотографий EPIC для скачивания', type=int, default=1)
    args = parser.parse_args()
    epic__number = args.EPIC
    try:
        conect_nasa_epic(epic__number, payload)
    except SyntaxError:
        print("<h1>SyntaxError: invalid syntax</h1>")
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")
    except NameError:
        print("По этой ссылке не фотом для скачивания")
