from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# import csv

url = "https://www.hollys.co.kr/menu/espresso.do"

dr = webdriver.Chrome("D:\chromeDriver\chromedriver.exe")
dr.get(url)

# fName = "hollys.csv"
# f = open(fName, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)

soup = BeautifulSoup(dr.page_source,"html.parser")

data = soup.find_all("div",attrs={"class":"tableType01"})
# print(data[0])

for info in data:
    name = info.select_one("caption").get_text()
    incoffe = info.select("tbody")
    for x in incoffe:
        reX = x.select("tr")
        for y in reX:
            output = [z.get_text() for z in y.select("td")]
            output.insert(0,name)
            print(output)


dr.quit()