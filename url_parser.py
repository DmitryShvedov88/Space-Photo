import os

from fetch_spacex_images import fetch_spacex_last_launch

def url_parser(name, date, i):
    date = datetime.datetime.fromisoformat(date)
    date = date.strftime("%Y/%m/%d")
    #print("i", i)
    #print("name: ", name)
    #print("date: ", date)
    find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key=DEMO_KEY'
    #print(find_url)
    fetch_spacex_last_launch(find_url, i)

def apod_parser(url_X, all_fotos, payload):
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