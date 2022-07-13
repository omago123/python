from bs4 import BeautifulSoup
from selenium import webdriver

import csv

url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2021&type=pitcher&playerOrder=era"

dr = webdriver.Chrome("chromedriver.exe")
dr.get(url)
hd = dr.page_source

fName = "Pitcher.csv"
f = open(fName, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "순위 선수 평균자책 경기수 이닝 승 패 세이브 홀드 탈삼진 피안타 피홈런 실점 볼넷 사구 승률"
title = title.split(" ")
writer.writerow(title)


soup = BeautifulSoup(hd, "html.parser")

mydata = soup.find("div", id="_pitcherRecord").find("table").find("tbody").find_all("tr")
for row in mydata:
    columns = row.find_all("th") + row.find_all("td")
    data = [column.get_text().strip() for column in columns]
    writer.writerow(data)