#this script download photo
import requests


def fetch_spacex_last_launch(find_url, i):
    print("find_url", find_url)
    filename = f'EPIC{i}.jpeg' #f'space_{value}.jpeg'
    print(filename)
    
    #Создание папки, если ее не существует
    try:
        path = Path(f"images/{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)

        response = requests.get(find_url) #, params=payload
        print("response.url:", response.url)
        print("response.status_code:", response.status_code)
        print("-------")
        with open(path, 'wb') as file:
            file.write(response.content)
    except:
        print("error")