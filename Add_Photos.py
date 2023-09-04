import datetime
import requests
import os
import urllib.parse

from pathlib import Path
from urllib.parse import urlparse


def fetch_spacex_last_launch(find_url, value):
    payload = {"api_key": os.getenv("Nasa_TOKEN")}
    #print("find_url", find_url)
    filename = f'space_{value}.jpeg'
    print(filename)
    path = Path(f"images/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(find_url, params=payload)
    print("response.url:", response.url)
    print("response:", response)
    with open(path, 'wb') as file:
        file.write(response.content)


def space_X(all_fotos, payload):
    response = requests.get(all_fotos, params=payload)
    print("response.url:", response.url)
    #print("response:", response)
    print("response.status_code:", response.status_code)
    #print("response.raise_for_status():", response.raise_for_status())
    text = response.json()
    print("-------")
    #print("text:", text)

    for i in range(5):
        try:
            for key, value in text[i].items():
                print(i)
                print(value)
                date = datetime.datetime.fromisoformat(value)
                image = date.strftime("%Y-%m-%d")
                print("image:", image)
                find_url = f'https://api.nasa.gov/EPIC/api/natural/date/{image}?api_key=DEMO_KEY'
                #print(find_url)
                #print(url_X)
                print("-----")
                fetch_spacex_last_launch(find_url, value)
            #else:
            #    continue
        except:
            continue


def url_parser(url_X, all_fotos, payload):
    parsed_link = urlparse(url_X)
    print("parsed_link:", parsed_link)
    path = parsed_link.path
    print("path:", path)
    splite_text = os.path.splitext(path)
    print("splite_text:", splite_text)
    execute = splite_text[-1]
    print(execute)
    print("  ")
    splite_text = os.path.basename(path)
    a = urlparse(url_X)
    print("splite_text:", splite_text)
    print("urllib.parse.unquote(splite_text):",
          urllib.parse.unquote(splite_text))
    print("a.path: ", a.path)
    way = (a.path).split('/')

    parsed_link.netloc
    api = way[2]
    image = "/".join(str(element) for element in way[4:9])
    #print(api)
    #print(image)
    find_url = f'https://api.nasa.gov/EPIC/{api}/natural/{image}?api_key=DEMO_KEY'
    print(find_url)
    print(url_X)


def test_response(ll_fotos, payload):
    urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    response = requests.get(url_X, params=payload)
    print("response.url:", response.url)
    print("response:", response)
    print("response.status_code:", response.status_code)
    print("response.raise_for_status():", response.raise_for_status())
    #text = response.json()
    print("-------")

    response = requests.get(all_fotos, params=payload)
    print("response.url:", response.url)
    print("response:", response)
    print("response.status_code:", response.status_code)
    print("response.raise_for_status():", response.raise_for_status())
    text = response.json()
    print("-------")
    #print("text:", text)
    for i in range(10):
        print(i, text[i])
        print("-------")
    url_parser(url_X, all_fotos, payload)


def main():
    from dotenv import load_dotenv, find_dotenv
    from urllib.parse import unquote
    load_dotenv(find_dotenv())
    name_url = "https://api.nasa.gov/planetary/apod?"
    #formation_url = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY"
    all_fotos = "https://api.nasa.gov/EPIC/api/natural/all?api_key=DEMO_KEY"
    payload = {"api_key": os.getenv("Nasa_TOKEN"), "count": "30"}
    space_X(all_fotos, payload)

    #for tests and analises
    aDate = datetime.date.fromisoformat('2020-10-04')
    #print(type(aDate))
    #test_response(all_fotos, payload)


if __name__ == "__main__":
    main()