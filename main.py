import argparse
from recive_photos import argument_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('--ID_launch', help='Введите --ID_launch номер запуска', type=str)
    parser.add_argument('--APOD', help='Введите --APOD и кол фотографий для скачивания', type=int, default=1)
    parser.add_argument('--EPIC', help='Введите --EPIC', type=int, default=1)
    args = parser.parse_args()
    params = {
        "ID_launch": args.ID_launch,
        "APOD": args.APOD,
        "EPIC": args.EPIC
    }
    for typer in params.items():
        if typer[1]:
            try:
                argument_handler(typer[0], typer[1])
            except:
                print("Ошибка ввода")
    if params["ID_launch"] is None and params["APOD"] is None and params["EPIC"] is None:
        typer = None
        launch = None
        argument_handler(typer, launch)
