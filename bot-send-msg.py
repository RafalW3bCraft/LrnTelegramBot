import requests
import json
import time

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFs"
url = f"https://api.telegram.org/bot{api_token}/sendMessage"

param = {
    "chat_id": "-4568794607",
    "text": "Hello Code World"
}

botapi = requests.get(url, data=param).json()
print(botapi['result']['text'])