import requests
import argparse
from download_image import download_image
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def take_links_id(all_starts) -> list:
    response = requests.get(all_starts)
    response.raise_for_status()
    text = response.json()
    links = text["links"]["flickr"]["original"]
    photo_name = "SpaceX"
    photo_format = "jpeg"
    if links:
        print("Ссылки есть")
        links = text["links"]["flickr"]["original"]
        for i, foto in enumerate(links):
            download_image(photo_name, photo_format, foto, i)
    else:
        print("Ссылок нет")


def conect_spacex(id_launch):
    if id_launch == "None":
        last_launch = "https://api.spacexdata.com/v5/launches/latest"
        take_links_id(last_launch)
    else:
        launch_number = f"https://api.spacexdata.com/v5/launches/{id_launch}"
        take_links_id(launch_number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument(
        '--ID_launch', help='Введите --ID_launch <номер запуска>', type=str, default=None
        )
    args = parser.parse_args()
    id_launch = format(args.ID_launch)
    if id_launch:
        try:
            conect_spacex(id_launch)
        except SyntaxError:
            print("<h1>SyntaxError: invalid syntax</h1>")
        except requests.exceptions.HTTPError:
            print("Вы ввели неправильную ссылку или неверный токен.")
        except NameError:
            print("По этой ссылке не фотом для скачивания")
