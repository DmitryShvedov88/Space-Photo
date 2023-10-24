import requests
import argparse
from recive_photos import take_links_id
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


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
