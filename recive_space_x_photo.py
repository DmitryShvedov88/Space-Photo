import requests
import argparse
from download_image import download_image


def take_links_id(id_launch) -> list:
    spacex_start = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    response = requests.get(spacex_start)
    response.raise_for_status()
    photos = response.json()
    links = photos["links"]["flickr"]["original"]
    photo_name, photo_format = "SpaceX", "jpeg"
    if not links:
        print("Ссылок нет")
        return
    print("Ссылки есть")
    for i, foto in enumerate(links):
        download_image(photo_name, photo_format, foto, i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии с сайта SpaceX'
        )
    parser.add_argument(
        '--launch_ID', help='Введите --launch_ID <номер запуска>', type=str, default="latest"
        )
    args = parser.parse_args()
    launch_id = format(args.launch_ID)
    take_links_id(launch_id)

