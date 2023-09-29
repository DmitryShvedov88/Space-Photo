import telegram
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


TG_Token = os.getenv("TG_Token")
chat_id = os.getenv("chat_id")
bot = telegram.Bot(token=TG_Token)
bot.send_message(chat_id=chat_id, text="Dima, i'll sand to you photo.")
bot.send_document(chat_id=chat_id, document=open('C:/Users/nivka/Desktop/Обучение Питон/Мои проекты/images/space_0.jpeg', 'rb'))

# updates = bot.get_updates()
# print([u.message.photo for u in updates if u.message.photo])
# if __name__ == "__main__":
#     bot.polling(none_stop=True, interval=0)