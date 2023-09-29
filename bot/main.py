import telegram
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


TG_Token = os.getenv("TG_Token")
chat_id = os.getenv("chat_id")
bot = telegram.Bot(token=TG_Token)
bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")


# if __name__ == "__main__":
#     bot.polling(none_stop=True, interval=0)