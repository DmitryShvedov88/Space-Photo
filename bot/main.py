import telegram
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


TG_Token = os.getenv("TG_Token")
bot = telegram.Bot(token = TG_Token)
print(bot.get_me())
