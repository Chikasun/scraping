import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.jpx.co.jp/listing/stocks/delisted/index.html")

soup = BeautifulSoup(r.content, "html.parser")

# ニュース一覧を抽出
# print(soup.find("div", "component-normal-table"))
# print(soup.findAll("td", "a-left"))
# print(soup.find("ul", "newsFeed_list").text)
i = 0
for item in soup.findAll("td", "a-left"):
    if i % 2 == 0:
        print(str(item.text) + str(i))
    i += 1
