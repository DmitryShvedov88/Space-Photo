import requests
import argparse
import os
from download_image import download_image
from dotenv import load_dotenv, find_dotenv


def take_apod_links(apod_link, payload) -> list:
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    photos_informarion = response.json()
    links = [photo_informarion["url"] for photo_informarion in photos_informarion]
    return links


def conect_nasa_apod(payload):
    apod_link = 'https://api.nasa.gov/planetary/apod'
    apod_photos_urls = take_apod_links(apod_link, payload)
    photo_name = "APOD"
    for number, apod in enumerate(apod_photos_urls):
        photo_format = "jpeg"
        download_image(photo_name, photo_format, apod, number)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии с сайта NASA'
        )
    parser.add_argument('APOD', help='Введите кол фотографий APOD для скачивания', type=int, default=1)
    args = parser.parse_args()
    apod_number = args.APOD
    payload = {"api_key": os.getenv("NASA_TOKEN"), "count": apod_number}
    try:
        conect_nasa_apod(payload)
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")
