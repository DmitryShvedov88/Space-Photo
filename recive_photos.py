import datetime
import requests
from download_image import download_image


def take_links_id(typer, all_starts) -> list:
    response = requests.get(all_starts)
    response.raise_for_status()
    text = response.json()
    links = text["links"]["flickr"]["original"]
    photo_format = "jpeg"
    if links:
        print("Ссылки есть")
        links = text["links"]["flickr"]["original"]
        try:
            for i, foto in enumerate(links):
                download_image(typer, photo_format, foto, i)
        except NameError:
            print("Скачивать нечего")
    else:
        print("Ссылок нет")


def take_links_apod(APOD_link, payload) -> list:
    response = requests.get(APOD_link, params=payload)
    response.raise_for_status()
    texts = response.json()
    links = list()
    for text in texts:
        url = text["url"]
        links.append(url)
    return [links, texts]


def take_links_epic(typer, EPIC_link, payload, count) -> list:
    response = requests.get(EPIC_link, params=payload)
    print("response.status_code", response.status_code)
    response.raise_for_status()
    print("response.status_code", response.status_code)
    texts = response.json()
    for i in range(count):
        try:
            name = texts[i]["image"]
            date = texts[i]["date"]
            date = datetime.datetime.fromisoformat(date)
            date = date.strftime("%Y/%m/%d")
            find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png'
            photo_format = "png"
            download_image(typer, photo_format, find_url, date)
        except requests.exceptions.HTTPError:
            continue
