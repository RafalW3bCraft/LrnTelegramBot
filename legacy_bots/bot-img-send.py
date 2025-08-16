import requests
import json
import time

api_token = "7926352569:AAFp9rQSEWf82zpaut_DQhNBbEeFs"
url = f"https://api.telegram.org/bot{api_token}/sendPhoto"

images = [
    ("https://images.unsplash.com/photo-1544890225-2f3faec4cd60?fit=max&fm=jpg&ixid=MnwzNTY3MHwwfDF8YWxsfHx8fHx8fHx8MTY2Nzg4NDQ1OQ&ixlib=rb-4.0.3&q=75&w=720&utm_medium=referral&utm_source=vocal.media", "Unsplash Image"),
    ("https://images.unsplash.com/photo-1502519144081-acca18599776?fit=max&fm=jpg&ixid=MnwzNTY3MHwwfDF8YWxsfHx8fHx8fHx8MTY2ODMxNjg2MQ&ixlib=rb-4.0.3&q=75&w=720&utm_medium=referral&utm_source=vocal.media", "Unsplash Image"),
    ("https://res.cloudinary.com/jerrick/image/upload/c_fill,d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,h_375,q_auto,w_625/670b8e50670e83001d5e9e7f.jpg", "Cloudinary Image"),
    ("https://res.cloudinary.com/jerrick/image/upload/c_fill,d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,h_375,q_auto,w_625/6704dccb4e72be001d0e677c.jpg", "Cloudinary Image"),
    ("https://res.cloudinary.com/jerrick/image/upload/c_fill,d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,h_375,q_auto,w_625/6703ced3773244001d40fb7b.jpg", "Cloudinary Image"),
    ("https://www.kaspersky.com/content/en-global/images/repository/isc/2017-images/web-img-13.jpg", "Kaspersky Image"),
    ("https://content.kaspersky-labs.com/fm/press-releases/d6/d6442301e2ac6fa8be14d731ad25a118/source/premiumbanner-04.jpg", "Kaspersky Premium Banner"),
    ("https://content.kaspersky-labs.com/fm/site-editor/8a/8a69dfb8f2cf9e25804b6e4fe40d3d95/processed/get-freeglobalbanner300x600-q93.gif", "Kaspersky Free Banner"),
    ("https://content.kaspersky-labs.com/se/com/content/en-global/images/homepage/kaspersky-logo/kaspersky-logo.svg", "Kaspersky Logo"),
    ("https://content.kaspersky-labs.com/fm/site-editor/2f/2f0a7404c547065a1fe6eb7754282ff9/processed/facebook.svg", "Facebook Icon"),
    ("https://content.kaspersky-labs.com/fm/site-editor/ad/ad34ec646b386d1a3c8fccd270d58bda/source/twitterx.svg", "Twitter Icon"),
    ("https://content.kaspersky-labs.com/fm/site-editor/6e/6e58acdcfdbd7ecb043da3fc03848651/processed/linkedin.svg", "LinkedIn Icon"),
    ("https://content.kaspersky-labs.com/fm/site-editor/5d/5d57477b76a23972f9ef486bf88a615d/processed/whatsapp.svg", "WhatsApp Icon"),
    ("https://camo.githubusercontent.com/d630f4e57d8a830620cbccace070d8b7def04f3c8ba312993efec9c06f28946b/687474703a2f2f692e696d6775722e636f6d2f3665764547374e2e706e67", "GitHub Image")
]
while True: # loop
  for image, caption in images:
    time.sleep(3)
    param = {
        "chat_id": "-4568794607",
        "photo": image,
        "caption": caption
        }
    botapi = requests.get(url, data=param).json()
    print(botapi)