import datetime
import requests
import os
from download_image import download_image


def take_links_id(all_starts) -> list:
    response = requests.get(all_starts)
    text = response.json()
    links = text["links"]["flickr"]["original"]
    if links is False:
        print("Фото не делались")

    else:
        print("Фото есть")
        links = text["links"]["flickr"]["original"]

    return links


def links_apod(APOD_pic, payload) -> list:
    response = requests.get(APOD_pic, params=payload)
    texts = response.json()
    links = list()
    for text in texts:
        url = text["url"]
        links.append(url)
    return links


def links_epic(typer, EPIC_pic, payload, count):
    response = requests.get(EPIC_pic, params=payload)
    texts = response.json()
    for i in range(count):
        try:
            name = texts[i]["image"]
            date = texts[i]["date"]
            date = datetime.datetime.fromisoformat(date)
            date = date.strftime("%Y/%m/%d")
            find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key=DEMO_KEY'
            download_image(typer, find_url, date)
        except:
            continue


def conect_spacex(typer, launch):
    if launch == "None":
            print(typer, launch)
            last_launch = "https://api.spacexdata.com/v5/launches/latest"
            links = take_links_id(last_launch)
            if len(links) > 0:
                for i in range(len(links)-3):
                    try:
                        foto = links[i]
                        download_image(typer, foto, i)
                    except:
                        continue
            else:
                print("Скачивать нечего")
    else:
        launch = f"https://api.spacexdata.com/v5/launches/{launch}"
        links = take_links_id(launch)
        if len(links) > 0:
            for i in range(len(links)-3):
                try:
                    foto = links[i]
                    download_image(typer, foto, i)
                except:
                    continue
        else:
            print("Скачивать нечего")


def conect_NASA_APOD(typer, launch):
    payload = {"api_key": os.getenv("Nasa_TOKEN"), "count": launch}
    apod_pic = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    apod_info = links_apod(apod_pic, payload)
    if len(apod_info) > 0:
        for i in range(len(apod_info)):
            try:
                find_url = apod_info[i]
                download_image(typer, find_url, i)
            except:
                continue
    else:
        print("Скачивать нечего")


def conect_NASA_EPIC(typer, count):
        payload = {"api_key": os.getenv("Nasa_TOKEN")}
        EPIC_pic = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
        links_epic(typer, EPIC_pic, payload, count)


def argument_handler(typer, launch):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    if typer == "ID_launch" or typer is None:
        conect_spacex(typer, launch)
    if typer == "APOD":
        conect_NASA_APOD(typer, launch)
    if typer == "EPIC":
        conect_NASA_EPIC(typer, launch)
