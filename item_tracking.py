from bs4 import BeautifulSoup
import requests
import time
import os
import webbrowser
from pynotifier import Notification

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.61 Safari/537.36"
}

url_to_item = input("Ссылка на предмет: ")
max_price = float(input("Введите максимальную стоимость предмета: "))


def get_html(url):
    response = requests.get(url, headers=headers)
    return response


opened = False


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="item hot")
    container = []
    for item in items:
        container.append({
            "price": float(item.find("div", class_="price").get_text(strip=True).replace(" ", "")),
            "url": "https://market.csgo.com" + str(item.get("href"))
        })
    for i in container:
        if i['price'] <= max_price:
            Notification(title="Item",
                         description=f"Item is ready to buy, open browser",
                         duration=10).send()
            webbrowser.open(i['url'])
            global opened
            opened = True


def parse():
    html = get_html(url_to_item)
    get_content(html.text)
    time.sleep(5)


while True:
    parse()
    if opened:
        break
