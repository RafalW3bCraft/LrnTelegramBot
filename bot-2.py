import requests
import json

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBeFs"
url = f"https://api.telegram.org/bot{api_token}/getUpdates"

botapi = requests.get(url).json()
print(botapi)

