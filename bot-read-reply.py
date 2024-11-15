import requests
import json
import time

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFsB"
url = f"https://api.telegram.org/bot{api_token}"

def get_msg(offset):
  param = {
      "offset": offset
  }
  botapi = requests.get(url + "/getUpdates", data=param).json()
  print(botapi)
  for result in botapi['result']:
    if 'Hello' in result['message']['text']:
      print('Get Message', result['message']['text'])
      send_msg()
  if botapi['result']:
    return botapi['result'][-1]['update_id'] + 1

def send_msg():
  param = {
      'chat_id': '-4568794607',
      'text': 'Hello Guest'
  }
  botapi = requests.get(url + "/sendMessage", data=param).json()
  print('Send Message', botapi['result']['text'])


offset = 0
while True:
  offset = get_msg(offset)
  time.sleep(3)