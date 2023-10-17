import requests
import argparse
import os
from recive_photos import links_apod
from dotenv import load_dotenv, find_dotenv
from download_image import download_image
load_dotenv(find_dotenv())


def conect_NASA_APOD(typer, launch):
    payload = {"api_key": os.getenv("Nasa_TOKEN"), "count": launch}
    apod_pic = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    apod_info = links_apod(apod_pic, payload)
    error_connection = apod_info[1]
    apod_info = apod_info[0]

    if len(apod_info) > 0:
        for i in range(len(apod_info)):
            try:
                find_url = apod_info[i]
                photo_format = "jpeg"
                download_image(typer, photo_format, find_url, i)
            except:
                continue
    else:
        print("Скачивать нечего")


def main(typer, launch):
    if typer == "APOD":
        try:
            conect_NASA_APOD(typer, launch)
        except requests.exceptions.HTTPError:
            print("Ошибка подключения")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('APOD', help='Введите --APOD и кол фотографий для скачивания', type=int, default=1)
    args = parser.parse_args()
    args = args.APOD
    typer = "APOD"
    try:
        main(typer, args)
    except:
        print("Ошибка ввода")
    if args is None:
        typer = None
        launch = None
        main(typer, launch)
