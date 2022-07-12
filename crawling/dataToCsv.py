import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"

fName = "test1.csv"
f = open(fName,"w",encoding="utf-8-sig", newline="")
writer = csv.writer(f)
res = requests.get(url)
res.raise_for_status()

title = "N 종목명 현재가 전일비 등락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER ROE "
title = title.split(" ")
writer.writerow(title)
soup = BeautifulSoup(res.text, "html.parser")

myData = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
for row in myData:
    columns = row.find_all("td")
    if len(columns) <=1:
        continue
    data = [column.get_text() for column in columns]
    writer.writerow(data)



