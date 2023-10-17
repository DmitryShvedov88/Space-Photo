import datetime
import requests
from download_image import download_image


def take_links_id(typer, all_starts) -> list:
    response = requests.get(all_starts)
    response.raise_for_status()
    text = response.json()
    links = text["links"]["flickr"]["original"]
    photo_format = "jpeg"
    if links is False:
        print("Ссылок нет")
    else:
        print("Ссылки есть")
        links = text["links"]["flickr"]["original"]
        if len(links) > 0:
            for i in range(len(links)-3):
                try:
                    foto = links[i]
                    download_image(typer, photo_format, foto, i)
                except:
                    continue
        else:
            print("Скачивать нечего")


def links_apod(APOD_pic, payload) -> list:
    response = requests.get(APOD_pic, params=payload)
    response.raise_for_status()
    texts = response.json()
    links = list()
    for text in texts:
        url = text["url"]
        links.append(url)
    return [links, texts]


def links_epic(typer, EPIC_pic, payload, count) -> list:
    response = requests.get(EPIC_pic, params=payload)
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
            print(name, date)
            find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key=DEMO_KEY'
            photo_format = "png"
            print(find_url)
            download_image(typer, photo_format, find_url, date)
        except:
            continue
