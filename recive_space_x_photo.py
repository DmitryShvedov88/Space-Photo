import requests
import argparse
from download_image import download_image
from dotenv import load_dotenv, find_dotenv


def take_links_id(id_launch) -> list:
    spacex_start = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    response = requests.get(spacex_start)
    response.raise_for_status()
    photos_informarion = response.json()
    links = photos_informarion["links"]["flickr"]["original"]
    photo_name = "SpaceX"
    photo_format = "jpeg"
    if links:
        print("Ссылки есть")
        links = photos_informarion["links"]["flickr"]["original"]
        for i, foto in enumerate(links):
            download_image(photo_name, photo_format, foto, i)
    else:
        print("Ссылок нет")


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии с сайта SpaceX'
        )
    parser.add_argument(
        '--ID_launch', help='Введите --ID_launch <номер запуска>', type=str, default="latest"
        )
    args = parser.parse_args()
    id_launch = format(args.ID_launch)
    if id_launch:
        try:
            take_links_id(id_launch)
        except SyntaxError:
            print("<h1>SyntaxError: invalid syntax</h1>")
        except requests.exceptions.HTTPError:
            print("Вы ввели неправильную ссылку или неверный токен.")
        except NameError:
            print("По этой ссылке не фотом для скачивания")
