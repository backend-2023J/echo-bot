import requests
from time import sleep

TOKEN='6388893107:AAGIbsoNExuuEgRirNnCbLQyN_wI9-9BrPA'

def getUpdates() -> list:
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    response = requests.get(url=BASE_URL)
    updates=response.json()['result']

    return updates

def sendMessage(chat_id:str, text:str):
    params = {
        "chat_id":chat_id,
        "text": text
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(URL, params=params)

    return response.status_code

last_number_of_message = -1

while True:
    updates = getUpdates()
    text = updates[-1]['message']['text']
    chat_id = updates[-1]['message']['chat']['id']
    number_of_message = len(updates)

    if number_of_message != last_number_of_message:
        sendMessage(chat_id, text)
        last_number_of_message = number_of_message
        print(number_of_message)

    sleep(1)