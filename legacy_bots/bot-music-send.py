import requests
import json
import time

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFs"
url = f"https://api.telegram.org/bot{api_token}/sendAudio"

audio_n_cap = [
    ("ChillVibes.wav", "Chillwave Vibes"),
    ("HourTriumph.wav", "Hour Of Triumph"),
    ("FantasyHeart.wav", "Fantasy of the Heart")
]
for audio, caption in audio_n_cap:
  time.sleep(3)
  with open(audio, 'rb') as audi:
    param = {
        "chat_id": "-4568794607",
        "caption": caption
        }
    files = {
        "audio": audi
    }
    botapi = requests.get(url, data=param, files=files).json()
    print(botapi)