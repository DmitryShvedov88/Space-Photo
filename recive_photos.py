import datetime
import requests
import os
from download_image import download_image

def links_id(all_starts) -> list:
    response = requests.get(all_starts)
    print("response.status_code:", response.status_code)
    print("response.raise_for_status():", response.raise_for_status())
    text = response.json()
    links = text["links"]["flickr"]["original"]
    if len(links) == 0:
        print("Фото не делались")

    else:
        print("Фото есть")
        links = text["links"]["flickr"]["original"]

    return links


def links_apod(APOD_pic, payload) -> list:
    response = requests.get(APOD_pic, params=payload)
    print("response.url:", response.url)
    print("response.raise_for_status():", response.raise_for_status())
    texts = response.json()
    links = list()
    for text in texts:
        url = text["url"]
        links.append(url)
    return links


def links_epic(EPIC_pic, payload, count):
    response = requests.get(EPIC_pic, params=payload)
    print("response.url:", response.url)
    print("response.status_code:", response.status_code)
    texts = response.json()
    for i in range(count):
        try:
            name = texts[i]["image"]
            date = texts[i]["date"]
            date = datetime.datetime.fromisoformat(date)
            date = date.strftime("%Y/%m/%d")
            find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key=DEMO_KEY'
            fetch_nasa_epic(find_url, date)
        except:
            continue


def argument_handler(typer, launch):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    if typer == "ID_launch" or typer is None:
        if launch is None:
            last_launch = "https://api.spacexdata.com/v5/launches/latest"
            links = links_id(last_launch)
            if len(links) > 0:
                for i in range(len(links)-3):
                    try:
                        foto = links[i]
                        fetch_spacex_images(foto, i)
                    except:
                        continue
            else:
                print("Скачивать нечего")
        else:
            print(launch)
            launch = f"https://api.spacexdata.com/v5/launches/{launch}"
            links = links_id(launch)
            if len(links) > 0:
                for i in range(len(links)-3):
                    try:
                        foto = links[i]
                        fetch_spacex_images(foto, i)
                    except:
                        continue
            else:
                print("Скачивать нечего")
    if typer == "APOD":
        payload = {"api_key": os.getenv("Nasa_TOKEN"), "count": launch}
        APOD_pic = f'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
        links = links_apod(APOD_pic, payload)
        print(links)
        if len(links) > 0:
            for i in range(len(links)):
                try:
                    find_url = links[i]
                    fetch_nasa_apod(find_url, i)
                except:
                    continue
        else:
            print("Скачивать нечего")
    if typer == "EPIC":
        payload = {"api_key": os.getenv("Nasa_TOKEN")}
        EPIC_pic = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
        links = links_epic(EPIC_pic, payload, launch)
