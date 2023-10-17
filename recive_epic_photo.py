import requests
import argparse
import os
from dotenv import load_dotenv, find_dotenv
from recive_photos import links_epic
load_dotenv(find_dotenv())


def conect_NASA_EPIC(typer, count):
    print(typer, count)
    payload = {"api_key": os.getenv("Nasa_TOKEN")}
    EPIC_pic = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    links_epic(typer, EPIC_pic, payload, count)


def main(typer, args):
    if typer == "EPIC":
        try:
            conect_NASA_EPIC(typer, args)
        except requests.exceptions.HTTPError:
            print("Ошибка подключения")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('EPIC', help='Введите --EPIC', type=int, default=1)
    args = parser.parse_args()
    args = args.EPIC
    typer = "EPIC"
    try:
        main(typer, args)
    except:
        print("Ошибка ввода")
    if args is None:
        typer = None
        count = None
        main(typer, count)
