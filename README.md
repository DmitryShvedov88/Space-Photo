## [Space Telegram](https://github.com/DmitryShvedov88/Space-Photo/blob/main/README.md#space-telegram "LINK TO THE PROJECT")

This program made for education putpose
It download photo from [Nasa](https://www.nasa.gov/), [Space_X](https://www.spacex.com/) and send it in telegram chanal
 
This program consists of two parts.
The first part is a three programs that allows you to upload photos on specified topics from NASA and SpaceX websites.
The second part is the publication of them in the Telegram channel.

### To upload a photo, you are given the opportunity to see what kind of photos they will be, using the necessary program.

First program: 'recive_space_x_photo' enter launch number for a photo from the SpaceX Website, if you don't, just start program, you will automatically get the newest.
    
    python recive_space_x_photo.py --ID_launch <launch number>

    example of running:
    python recive_space_x_photo.py --ID_launch 5eb87d47ffd86e000604b38a
    program response:
    Ссылки есть
    Ссылок нет

Second program: 'recive_apod_photo' enter number of APOD photos you would to download from NASA site.
    
    python recive_apod_photo.py <number of photos>
    
    example of running:
    python recive_apod_photo.py 1
    program response:
    download image in folder
    
Third program: 'recive_epic_photo' enter number of EPIC photos you would to download from NASA site.
    
    python recive_epic_photo.py <number of photos>
    
    example of running:
    python recive_epic_photo.py 1
    program response:
    download image in folder

The second part sends photos from the list to the telegram channel. You can set the time how often the photos will be published. If you do not set a timer, by default it will happen once every 4 hours.

Fourth program: "photo_pusher" serves to publish photos in a telegram bot to a group. The program publishes photos once in the specified time interval at startup
    
    python photo_push.py --time <how often to publish>

    example of running:
    python photo_pusher.py 1
    program response:
    push image on TG bot channal


### How to check
A folder will be created on the computer in the selected directory and photos will be uploaded there.
The second part sends photos in TG-chanel.

### How to install
Python3 should already be installed.
Use pip (or pip3, if there is a conflict with Python2) to install dependencies.
    
    pip install -r requirements.txt

### environment variables
For the program to function, you will need the following environment variables: NASA_TOKEN, TG_TOKEN, CHAT_ID.

NASA_TOKEN - is the digital key needed to run two programs: recive_apod_photo, recive_epic_photo.
You can get it [here](https://api.nasa.gov/)

TG_TOKEN - is the digital key needed to run TG Bot
You can get it using [Botfather](https://t.me/BotFather) 

CHAT_ID - is a number of chat, where you want to push photo.
It s easy to find it is the name of the bot after @. "@BOT_NAME"

### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
