def url_parser(name, date, i):
    date = datetime.datetime.fromisoformat(date)
    date = date.strftime("%Y/%m/%d")
    #print("i", i)
    #print("name: ", name)
    #print("date: ", date)
    find_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key=DEMO_KEY'
    #print(find_url)
    fetch_spacex_last_launch(find_url, i)