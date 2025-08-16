import requests
import json

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFs"

# Fetch updates (messages) from the bot
url = f"https://api.telegram.org/bot{api_token}/getUpdates"
param = {
    "offset": "7707282225",
    "limit": "5"
}
botapi = requests.get(url, data=param).json()

# Check if the response is okay and has results
if botapi.get('ok'):
  gtxt = []
  for msg in botapi['result']:
    gtxt.append(msg['message']['text'])
  print(gtxt)
else:
    print("Error fetching updates:", botapi)