import requests
import argparse
import os
from recive_photos import take_links_epic


def conect_NASA_EPIC(count):
    payload = {"api_key": os.getenv("NASA_TOKEN")}
    EPIC_link = "https://api.nasa.gov/EPIC/api/natural/images"
    take_links_epic(EPIC_link, payload, count)


if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('EPIC', help='Введите --EPIC', type=int, default=1)
    args = parser.parse_args()
    args = args.EPIC
    try:
        conect_NASA_EPIC(args)
    except SyntaxError:
        print("SyntaxError ошибка ввода")
    except requests.exceptions.HTTPError:
        print("Ошибка подключения")
    except NameError:
        print("Скачивать нечего")
