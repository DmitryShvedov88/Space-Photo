import argparse
from recive_photos import argument_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии по заданным темам с сайтов NASA и SpaceX'
        )
    parser.add_argument('--EPIC', help='Введите --EPIC', type=int, default=1)
    args = parser.parse_args()
    args = format(args.EPIC)
    typer = "EPIC"
    try:
        argument_handler(typer, args)
    except:
        print("Ошибка ввода")
    if args is None:
        typer = None
        launch = None
        argument_handler(typer, launch)
