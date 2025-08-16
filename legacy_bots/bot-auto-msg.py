import requests
import json
import time

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFs"
url = f"https://api.telegram.org/bot{api_token}/sendMessage"

text = ["I don’t need luck. I make my own.",
   "The moment you start doubting me is the moment you’ve already lost.",
   "I didn’t come here to play games. I came here to win.",
   "You want to test me? Bring it. I’ve got nothing to lose.",
   "Failure? Not in my vocabulary.",
   "I don’t break rules. I rewrite them.",
   "Cross me once, and you’ll regret it forever.",
   "I’m not here to be nice. I’m here to be legendary.",
   "Some fight for survival. I fight to dominate.",
   "I don’t start fights, but I finish them.",
   "I’m not the hero. I’m the storm.",
   "Step aside. You’re in my way.",
   "Winning isn’t everything. It’s the only thing."
]

while True: # loop
  for t in text:
    time.sleep(13)
    param = {
        "chat_id": "-4568794607",
        "text": t
        }
    botapi = requests.get(url, data=param).json()
    print(botapi['result']['text'])

