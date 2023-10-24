import requests
import argparse
import os
from recive_photos import take_links_epic
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def conect_nasa_epic(count, payload):
    epic_link = "https://api.nasa.gov/EPIC/api/natural/images"
    take_links_epic(epic_link, payload, count)


if __name__ == "__main__":
    payload = {"api_key": os.getenv("NASA_TOKEN")}
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('EPIC', help='Введите --EPIC', type=int, default=1)
    args = parser.parse_args()
    args = args.EPIC
    try:
        conect_nasa_epic(args, payload)
    except SyntaxError:
        print("Не верно введена ссылка")
    except requests.exceptions.HTTPError:
        print("Ошибка подключения")
    except NameError:
        print("Скачивать нечего")
