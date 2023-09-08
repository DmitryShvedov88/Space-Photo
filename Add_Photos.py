import datetime
import requests
import os
import urllib.parse

from pathlib import Path
from urllib.parse import urlparse
from fetch_spacex_images import fetch_spacex_last_launch


        

    # links=text["links"]["flickr"]["original"]
    # print("links", links)
    # print("-------")
    # for i in range(len(links)):
    #     try:
    #         foto=links[i]
    #         parsed_link = urlparse(foto)
    #         print("parsed_link:", parsed_link)
    #         path = parsed_link.path
    #         print("path:", path)
    #         splite_text = os.path.splitext(path)
    #         print("splite_text:", splite_text)
    #         fetch_spacex_last_launch(foto, i)               
    #     except:
    #         continue





def test_response(all_starts): 
    #, payload):
    #urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    response = requests.get(all_starts) #, params=payload)
    print("response.url:", response.url)
    print("response:", response)
    print("response.status_code:", response.status_code)
    print("response.raise_for_status():", response.raise_for_status())
    text = response.json()
    # for text in texts:
    #     print(text.values())
    #     print("-------")
    links=text["links"]["flickr"]["original"]
    print("links", links)

                            
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


def main():
    from dotenv import load_dotenv, find_dotenv
    from urllib.parse import unquote
    load_dotenv(find_dotenv())
    
    payload = {"api_key": os.getenv("Nasa_TOKEN"), "count": "3"}
    # все по загрузке единичной картинке
    # url_for_downlod="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    # path="images"
    # для загрузки картинок через запрос 
    # fetch_spacex_last_launch(url_for_downlod, path)
    
    # ссылкка по всем запускам или последним
    #all_starts="https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    #test_response(all_starts)

    #загрузка картинки дня
    # APOD="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    # test_response(APOD, payload)
    
    #formation_url = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY"
    #all_fotos = "https://api.nasa.gov/EPIC/api/natural/all?api_key=DEMO_KEY"
    
    
    #для считывания нескольких картинок APOD
    # APOD_pic=f'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    # space_X(APOD_pic, payload)

    #for tests and analises
    #aDate = datetime.date.fromisoformat('2020-10-04')
    #print(type(aDate))
    #для считывания EPIC ссылки
    EPIC_pic="https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    space_X(EPIC_pic, payload)