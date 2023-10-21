import requests
import argparse
import os
from recive_photos import take_links_apod
from download_image import download_image


def conect_NASA_APOD(payload):
    apod_link = 'https://api.nasa.gov/planetary/apod'
    apod_info = take_links_apod(apod_link, payload)
    print(apod_info)
    error_connection = apod_info[1]
    apod_info = apod_info[0]
    photo_name = "APOD"
    if apod_info:
        print("Ссылки есть")
        try:
            for i, apod in enumerate(apod_info):
                photo_format = "jpeg"
                download_image(photo_name, photo_format, apod, i)
        except:
            print("Скачивать нечего")
    else:
        print("Ссылок нет")


def main(launch):
    payload = {"api_key": os.getenv("NASA_TOKEN"), "count": launch}
    try:
        conect_NASA_APOD(payload)
    except requests.exceptions.HTTPError:
        print("Ошибка подключения")


if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('APOD', help='Введите APOD и кол фотографий для скачивания', type=int, default=1)
    args = parser.parse_args()
    args = args.APOD
    try:
        main(args)
    except SyntaxError:
        print("SyntaxError ошибка ввода")
