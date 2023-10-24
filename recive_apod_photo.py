import requests
import argparse
import os
from recive_photos import take_links_apod
from download_image import download_image
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def conect_nasa_apod(payload):
    apod_link = 'https://api.nasa.gov/planetary/apod'
    apod_info = take_links_apod(apod_link, payload)
    apod_info = apod_info[0]
    photo_name = "APOD"
    if apod_info:
        print("Ссылки есть")
        for i, apod in enumerate(apod_info):
            photo_format = "jpeg"
            download_image(photo_name, photo_format, apod, i)
    else:
        print("Ссылок нет")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('APOD', help='Введите APOD и кол фотографий для скачивания', type=int, default=1)
    args = parser.parse_args()
    args = args.APOD
    payload = {"api_key": os.getenv("NASA_TOKEN"), "count": args}
    try:
        conect_nasa_apod(payload)
    except SyntaxError:
        print("Не верно введена ссылка")
    except requests.exceptions.HTTPError:
        print("Ошибка подключения")
    except NameError:
        print("Скачивать нечего")
