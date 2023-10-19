import requests
import argparse
import os
from recive_photos import links_apod
from dotenv import load_dotenv, find_dotenv
from download_image import download_image
load_dotenv(find_dotenv())


def conect_NASA_APOD(typer, payload):
    apod_pic = 'https://api.nasa.gov/planetary/apod'
    apod_info = links_apod(apod_pic, payload)
    print(apod_info)
    error_connection = apod_info[1]
    apod_info = apod_info[0]
    if apod_info:
        print("Ссылки есть")
        try:
            for i, apod in enumerate(apod_info):
                photo_format = "jpeg"
                download_image(typer, photo_format, apod, i)
        except:
            print("Скачивать нечего")
    else:
        print("Ссылок нет")


def main(typer, launch):
    payload = {"api_key": os.getenv("NASA_TOKEN"), "count": launch}
    if typer == "APOD":
        try:
            conect_NASA_APOD(typer, payload)
        except requests.exceptions.HTTPError:
            print("Ошибка подключения")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('APOD', help='Введите APOD и кол фотографий для скачивания', type=int, default=1)
    args = parser.parse_args()
    args = args.APOD
    typer = "APOD"
    try:
        main(typer, args)
    except SyntaxError:
        print("SyntaxError ошибка ввода")
