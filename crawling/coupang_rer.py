import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from ReObject import ReObject

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81"

dr = webdriver.Chrome("chromedriver.exe")
dr.get(url)
myData = dr.page_source

with open("coupang.html", "w", encoding="utf8") as f:
    f.write(myData)

dr.quit()

soup = BeautifulSoup(myData, "html.parser")
researchData = soup.select(".search-product-wrap")

resultDatas = []

for idx, item in enumerate(researchData):
    ra = 0.0
    rc = 0
    if researchData[idx].select(".rating"):
        ra = float(researchData[idx].select(".rating")[0].get_text())
        rc = int(researchData[idx].select(".rating-total-count")[0].get_text()[1:-1])
    else:
        ra = "평점 없음"
        rc = "리뷰 없음"
    # ndata = {
    #     "모델명" : researchData[idx].select(".name")[0].get_text(),
    #     "가격" : int(researchData[idx].select(".price-value")[0].get_text().replace(",","")),
    #     "평점" : ra,
    #     "리뷰" : rc
    # }
    mo = ReObject(researchData[idx].select(".name")[0].get_text(),int(researchData[idx].select(".price-value")[0].get_text().replace(",","")),ra,rc)
    resultDatas.append(mo)

for result in resultDatas:
    print(result.model_name, result.price, result.rank)