import datetime
import requests
import os
from download_image import download_image


def take_links_id(typer, all_starts) -> list:
    response = requests.get(all_starts)
    text = response.json()
    links = text["links"]["flickr"]["original"]
    if links is False:
        print("Ссылок нет")

    else:
        print("Ссылки есть")
        links = text["links"]["flickr"]["original"]
        if len(links) > 0:
            for i in range(len(links)-3):
                try:
                    foto = links[i]
                    download_image(typer, foto, i)
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


def links_epic(typer, EPIC_pic, payload, count):
    response = requests.get(EPIC_pic, params=payload)
    print(response.status_code)
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
    return response.json()


def conect_spacex(typer, launch):
    if launch == "None":
        last_launch = "https://api.spacexdata.com/v5/launches/latest"
        response = requests.get(last_launch)
        response.raise_for_status()
        take_links_id(typer, last_launch)
    else:
        launch = f"https://api.spacexdata.com/v5/launches/{launch}"
        response = requests.get(last_launch)
        response.raise_for_status()
        take_links_id(typer, launch)
    return response.json()


def conect_NASA_APOD(typer, launch):
    payload = {"api_key": os.getenv("Nasa_TOKEN"), "count": launch}
    apod_pic = 'https://api.nasa.gov/planetary/apo?api_key=DEMO_KEY'
    apod_info = links_apod(apod_pic, payload)
    error_connection = apod_info[1]
    apod_info = apod_info[0]

    if len(apod_info) > 0:
        for i in range(len(apod_info)):
            try:
                find_url = apod_info[i]
                download_image(typer, find_url, i)
            except:
                continue
    else:
        print("Скачивать нечего")
    return error_connection


def conect_NASA_EPIC(typer, count):
        payload = {"api_key": os.getenv("Nasa_TOKEN")}
        EPIC_pic = "https://api.nasa.gov/EPI/api/natural/images?api_key=DEMO_KEY"
        error_connection = links_epic(typer, EPIC_pic, payload, count)
        print("error_connection", error_connection)
        return error_connection

def argument_handler(typer, launch):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    if typer == "ID_launch" or typer is None:
        try:
            conect_spacex(typer, launch)
        except requests.exceptions.HTTPError:
            print("Ошибка подключения")
    if typer == "APOD":
        try:
            conect_NASA_APOD(typer, launch)
        except requests.exceptions.HTTPError:
            print("Ошибка подключения")
    if typer == "EPIC":
        try:
            conect_NASA_EPIC(typer, launch)
        except requests.exceptions.HTTPError:
            print("Ошибка подключения")
