import requests
import argparse
import os
from recive_photos import taker_epic_links
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


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
