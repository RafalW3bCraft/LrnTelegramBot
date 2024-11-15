import requests

# botapi = requests.get("https://api.telegram.org/bot7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFsBYOdVI/getUpdates?offset=770728217")
# print(botapi.text)


baseurl = "https://api.telegram.org/bot7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFs/getUpdates"

param = {
    "offset": "770728217",
    "limit": "3"
}

botapi = requests.get(baseurl, data=param)
print(botapi.text)
