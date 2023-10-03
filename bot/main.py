import argparse
import telegram
import time
import os
import random
from dotenv import load_dotenv, find_dotenv
from image_taker import takeFiles

load_dotenv(find_dotenv())


TG_Token = os.getenv("TG_Token")
chat_id = os.getenv("chat_id")
bot = telegram.Bot(token=TG_Token)


def main(timer):
    timer = timer*60
    images = takeFiles()
    i = 0
    while True:
        if i < len(images):
            for i in range(len(images)):
                time.sleep(timer)
                image = images[i]
                print(image)
                i+=1
                #bot.send_message(chat_id=chat_id, text="Dima, i'll sand to you photo.")
                bot.send_document(chat_id=chat_id, document=open(f'{image}', 'rb'))
        else:
            time.sleep(timer)
            l = random.randint(0, (len(images)-1))
            image = images[l]
            print(image)
            bot.send_document(chat_id=chat_id, document=open(f'{image}', 'rb'))
            
    #updates = bot.get_updates()
    #print([u.message.photo for u in updates if u.message.photo])
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии из деревтории в ТГ Бот'
        )
    parser.add_argument('--Time', help='Введите --Time ожидания публикации', type=int)
    args = parser.parse_args()
    params = {
        "Time": args.Time,
        } 
    for typer in params.items():
        if typer[1]:
            try:
                main(typer[1])
            except:
                print("Ошибка ввода")

    if params["Time"] is None:
        main(timer=4)
