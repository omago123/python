from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl ="https://www.youtube.com/results?search_query="
searchQuery = input("검색하세요 : ")
sUrl = baseUrl + searchQuery
print(sUrl)
dr = webdriver.Chrome("/Users/admin/crawling/chromedriver")
dr.get(sUrl)
hd = dr.page_source
bs_data = BeautifulSoup(hd, "html.parser")

myData = bs_data.select("#video-title")

for x in myData:
    print(x.get("title"))
    print(x.get("href").split("=")[1])
    print("-"*50)

dr.close()
