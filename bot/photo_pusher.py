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


def send_photo(timer):
    transfer_coefficient = 60
    timer = timer*transfer_coefficient
    images = takefiles(directory)
    i = 0
    for number, image in enumerate(images):
        if number <= len(images):
            time.sleep(timer)
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
        send_photo(typer[1])
