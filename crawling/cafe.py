from bs4 import BeautifulSoup
from selenium import webdriver
import csv
url="https://www.hollys.co.kr/menu/espresso.do"

dr = webdriver.Chrome("chromedriver.exe")
dr.get(url)
hd = dr.page_source


dr.close()


soup = BeautifulSoup(hd, "html.parser")

result = soup.select("#contents .center_t")
#
#
for x in result:
    print(x.get_text())

# name = soup.find_all("caption")
# for x in name:
#     print(x.get_text())
# print(name)

# for idx, x in enumerate(result):
#     print(x.select(".center_t")[idx].get_text())
#     print(idx)






