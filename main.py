import requests
from time import sleep

TOKEN='6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'

def getUpdates() -> list:
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    response = requests.get(url=url)
    updates=response.json()['result']

    return updates

def sendMessage(chat_id:str, text:str, ):
    params = {
        "chat_id":chat_id,
        "text": text
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url, params=params)

def sendPhoto(chat_id:str,photo:str):
    params = {
        "chat_id": chat_id,
        "photo": photo
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    response = requests.get(URL, params = params)
    return response.json()

last_message_id = -1

while True:
    updates = getUpdates()

    message_id = updates[-1]['message']['message_id']
    
    message = updates[-1]['message']
    chat_id = updates[-1]['message']['chat']['id']

    print(f"MESSAGE ID: {message_id}  LAST MESSAGE ID: {last_message_id}")

    if message_id != last_message_id:
        text = message.get('text')
        photo = message.get('photo')
        if text != None:
            if text == "/start":
                
                sendMessage(chat_id, "welcome to bot!")
            else:   
                sendMessage(chat_id, text)
        elif photo != None:
            file_id = photo[0]['file_id']
            sendPhoto(chat_id, file_id)
        else:
            sendMessage(chat_id, f"other format")

        last_message_id = message_id

    sleep(2)
