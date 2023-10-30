import argparse
import telegram
import time
import os
import random
from dotenv import load_dotenv, find_dotenv
from image_taker import takefiles


def send_photo(timer):
    timer = timer*60
    images = takefiles(directory)
    i = 0
    while True:
        if i < len(images):
            for i in range(len(images)):
                time.sleep(timer)
                image = images[i]
                print(image)
                i += 1
                bot.send_document(
                    chat_id=chat_id, document=open(f'{image}', 'rb')
                    )
        else:
            time.sleep(timer)
            random_number = random.randint(0, (len(images)-1))
            image = images[random_number]
            bot.send_document(chat_id=chat_id, document=open(f'{image}', 'rb'))


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    TG_Token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    directory = os.getenv("DIRECTORY")
    bot = telegram.Bot(token=TG_Token)
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии из деревтории в ТГ Бот'
        )
    parser.add_argument(
        '--Time',
        help='Введите --Time ожидания публикации',
        type=int,
        default=4
        )
    args = parser.parse_args()
    params = {
        "Time": args.Time,
        }
    for typer in params.items():
        try:
            send_photo(typer[1])
        except:
            send_photo("Ошибка ввода")
