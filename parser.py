from bs4 import BeautifulSoup
import requests
import time

lowest_price = str(input("low price: "))
highest_price = str(input("max price: "))
url = f"https://market.csgo.com/?s=pop&r=&q=&rs={lowest_price};{highest_price}&h="
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}


def get_html(url):
    response = requests.get(url, headers=headers)
    return response


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="item hot")
    container = []
    for item in items:
        container.append({
            "name": item.find("div", class_="name").get_text(strip=True),
            "price": item.find("div", class_="price").get_text(strip=True),
            "url": "https://market.csgo.com" + str(item.get("href"))
        })

    for items in container:
        for key, value in items.items():
            print(key + " -> " + value)
        print("---------------------------------------------" * 3)

    time.sleep(360)


def parse():
    html = get_html(url)
    get_content(html.text)


while True:
    parse()