import datetime
import requests
import os
import urllib.parse

from urllib.parse import urlparse
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic


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

def links_epic(EPIC_pic, payload, launch):
    response = requests.get(EPIC_pic, params=payload)
    print("response.url:", response.url)
    print("response.status_code:", response.status_code)
    texts = response.json()
    #print(texts)
    for i in range(int(launch)):
        #print(texts[i])
        #print("-------")
        try:
            name = texts[i]["image"]
            #print("name: ", name)
            value = texts[i]["date"]
            date = datetime.datetime.fromisoformat(value)
            date = date.strftime("%Y/%m/%d")
            #print("date:", date)
            find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key=DEMO_KEY'
            #print(find_url)
            #print("-----")
            fetch_nasa_epic(find_url, date)
        
        except:
            continue


def main(typer, launch):
    from dotenv import load_dotenv, find_dotenv
    from urllib.parse import unquote
    load_dotenv(find_dotenv())  
    print(typer, launch)
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
        #для считывания нескольких картинок APOD
        APOD_pic=f'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
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
        #print("typer:", typer, "launch", launch)
        payload = {"api_key": os.getenv("Nasa_TOKEN")}
        #для считывания нескольких картинок APOD
        EPIC_pic="https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
        links = links_epic(EPIC_pic, payload, launch)
        # if len(links) > 0:
        #     for i in range(len(links)):
        #         try:
        #             find_url = links[i]
        #             fetch_nasa_apod(find_url, i)
        #         except:
        #             continue
        # else:
        #     print("Скачивать нечего")


    # EPIC_pic="https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    # space_X(EPIC_pic, payload)


    # response = requests.get(all_starts) #, params=payload)
    # print("response.url:", response.url)
    # print("response:", response)
    # print("response.status_code:", response.status_code)
    # print("response.raise_for_status():", response.raise_for_status())
    # text = response.json()
    # print("-------")
    #print("text:", text)
    # for i in range(10):
    #     print(i, text[i])
    #     print("-------")
    # url_parser(url_X, all_fotos, payload)





    # все по загрузке единичной картинке
    # url_for_downlod="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    # path="images"

    # для загрузки картинок через запрос 
    # fetch_spacex_last_launch(url_for_downlod, path)
    
    
  
    #formation_url = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY"
    #all_fotos = "https://api.nasa.gov/EPIC/api/natural/all?api_key=DEMO_KEY"
       
    

    #for tests and analises
    #aDate = datetime.date.fromisoformat('2020-10-04')
    #print(type(aDate))
    #для считывания EPIC ссылки

    