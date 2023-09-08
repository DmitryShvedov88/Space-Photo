def space_X(EPIC_pic, payload):
    response = requests.get(EPIC_pic, params=payload)
    print("response.url:", response.url)
    print("response.status_code:", response.status_code)
    #print("response.raise_for_status():", response.raise_for_status())
    texts = response.json()
    print("-------")
    #print(texts)
    for i in range(3): #len(texts)
        name = texts[i]['image']
        #print("name: ", name)
        date = texts[i]['date']
        #print("date: ", date)
        url_parser(name, date, i)
