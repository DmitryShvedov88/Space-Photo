import argparse
import telegram
import time
import os
import random
from dotenv import load_dotenv, find_dotenv


def takefiles(directory):
    images = []
    filesindir = os.listdir(directory)
    for filesindirs in filesindir:
        name = os.path.join(filesindirs)
        path = os.path.join(str(directory), name)
        images.append(path)
    return images


def send_photos(timer):
    transfer_coefficient = 10
    timer = timer*transfer_coefficient
    images = takefiles(directory)
    while True:
        for image in images:
            time.sleep(timer)
            with open(image, 'rb') as img:
                bot.send_document(chat_id=chat_id, document=img)
        time.sleep(timer)
        random_number = random.shuffle(images)
        image = images[random_number]
        with open(image, 'rb') as img:
            bot.send_document(chat_id=chat_id, document=img)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    tg_token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    directory = os.getenv("DIRECTORY")
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(
        description='Программа позволяет загружать фотографии из деревтории в ТГ Бот'
        )
    parser.add_argument(
        '--time',
        help='Введите --time ожидания публикации',
        type=int,
        default=4
        )
    args = parser.parse_args()
    timer = args.time
    send_photos(timer)
