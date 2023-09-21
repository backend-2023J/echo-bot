import requests
from time import sleep

TOKEN='6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'

def getUpdates() -> list:
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    response = requests.get(url=url)
    updates=response.json()['result']

    return updates

def sendMessage(chat_id:str, text:str, parse_mode):
    params = {
        "chat_id":chat_id,
        "text": text,
        "parse_mode": parse_mode
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url, params=params)

last_message_id = -1

while True:
    updates = getUpdates()

    message_id = updates[-1]['message']['message_id']
    
    text = updates[-1]['message']['text']
    chat_id = updates[-1]['message']['chat']['id']

    print(f"MESSAGE ID: {message_id}  LAST MESSAGE ID: {last_message_id}")

    if message_id != last_message_id:
        sendMessage(chat_id, f"<i>{text}</i>",parse_mode="HTML")
        last_message_id = message_id

    sleep(2)
