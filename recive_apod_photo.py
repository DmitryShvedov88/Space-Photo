import argparse
from recive_photos import argument_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('--APOD', help='Введите --APOD и кол фотографий для скачивания', type=int, default=1)
    args = parser.parse_args()
    args = args.APOD
    typer = "APOD"
    try:
        argument_handler(typer, args)
    except:
        print("Ошибка ввода")
    if args is None:
        typer = None
        launch = None
        argument_handler(typer, launch)