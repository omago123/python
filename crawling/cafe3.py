from bs4 import BeautifulSoup
from selenium import webdriver

url="https://www.hollys.co.kr/menu/espresso.do"

dr = webdriver.Chrome("chromedriver.exe")
dr.get(url)
hd = dr.page_source

dr.close()

data = BeautifulSoup(hd, "html.parser")
name = data.select(".content")
print(name)
# for x in data:
#     x.select("caption")
#     for n in x:
#         print(n.get_text())
#


# for info in data:
#     incoffe = info.select("tbody")
#     for x in incoffe:
#         reX = x.select("tr")
#         for y in reX:
#             output = [z.get_text() for z in y.select("td")]
#             print(output)
#


