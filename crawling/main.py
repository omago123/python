import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import *


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# sp = BeautifulSoup(res.text, "html.parser")

# print(len(res.text))

# with open("webtoon.html", "w",encoding="utf8") as f:
#     f.write(res.text)
soup = BeautifulSoup(res.text, "html.parser")
# myList = soup.ol.select("li")

myList = soup.ol.select("li")

# for x in myList:
#     y = x["onclick"].split(",")[3][1:-2]
#     print(f"Rank {y} : {x.get_text()}")

for x in myList:
    print(x["class"][0],x.select("a")[0].get_text())

