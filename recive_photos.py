import datetime
import requests
from download_image import download_image


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


def taker_apod_links(apod_link, payload) -> list:
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    texts = response.json()
    links = [text["url"] for text in texts]
    return [links, texts]


def taker_epic_links(epic_link, payload, epic__number) -> list:
    response = requests.get(epic_link, params=payload)
    response.raise_for_status()
    texts = response.json()
    for number in range(epic__number):
        name = texts[number]["image"]
        date = texts[number]["date"]
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime("%Y/%m/%d")
        find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png'
        photo_name = "EPIC"
        photo_format = "png"
        download_image(photo_name, photo_format, find_url, date)
