import requests
import argparse
from recive_photos import take_links_id
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def conect_spacex(typer, launch):
    if launch == "None":
        last_launch = "https://api.spacexdata.com/v5/launches/latest"
        take_links_id(typer, last_launch)
    else:
        launch_number = f"https://api.spacexdata.com/v5/launches/{launch}"
        take_links_id(typer, launch_number)


def main(typer, launch):
    try:
        conect_spacex(typer, launch)
    except requests.exceptions.HTTPError:
        print("Ошибка подключения")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('--ID_launch', help='Введите --ID_launch номер запуска', type=str)
    args = parser.parse_args()
    args = format(args.ID_launch)
    typer = "ID_launch"
    if args:
        try:
            main(typer, args)
        except:
            print("Ошибка ввода")
    if args is None:
        typer = None
        launch = None
        main(typer, launch)
