import requests
import argparse
import os
from download_image import download_image
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def taker_apod_links(apod_link, payload) -> list:
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    texts = response.json()
    links = [text["url"] for text in texts]
    return links


def conect_nasa_apod(payload):
    apod_link = 'https://api.nasa.gov/planetary/apod'
    apod_info = taker_apod_links(apod_link, payload)
    photo_name = "APOD"
    for number, apod in enumerate(apod_info):
        photo_format = "jpeg"
        download_image(photo_name, photo_format, apod, number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('APOD', help='Введите кол фотографий APOD для скачивания', type=int, default=1)
    args = parser.parse_args()
    apod_number = args.APOD
    payload = {"api_key": os.getenv("NASA_TOKEN"), "count": apod_number}
    try:
        conect_nasa_apod(payload)
    except SyntaxError:
        print("<h1>SyntaxError: invalid syntax</h1>")
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")
    except NameError:
        print("По этой ссылке нет фото для скачивания")
