# ライブラリを取り込む --- (*1)
import openpyxl as excel
import requests
from bs4 import BeautifulSoup

# 新規ワークブックを作る --- (*2)
wb = excel.Workbook()
# アクティブなワークシートを得る --- (*3)
ws = wb.active

r = requests.get("https://www.jpx.co.jp/listing/stocks/delisted/index.html")

soup = BeautifulSoup(r.content, "html.parser")

# ニュース一覧を抽出
# print(soup.find("div", "component-normal-table").text)
hoge = soup.find("div", "component-normal-table").get_text(',', strip=True)
# print(hoge)
hogege = hoge.split(',')
#
print(hogege)
i = 1
j = 1
for item in hogege:
    print(item)
    ws.cell(row=i, column=j).value = item
    if j % 5 == 0:
        i += 1
        j = 1
    else:
        j += 1
# A1のセルに値を設定 --- (*4)
# ファイルを保存 --- (*5)
wb.save("hello.xlsx")
# print(soup.findAll("td", "a-left"))
# print(soup.find("ul", "newsFeed_list").text)
# i = 0
# for item in soup.findAll("td", "a-left"):
#     if i % 2 == 0:
#         print(str(item.text) + str(i))
#     i += 1
#
