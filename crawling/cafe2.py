from bs4 import BeautifulSoup
from selenium import webdriver

url="https://www.hollys.co.kr/menu/espresso.do"

dr = webdriver.Chrome("chromedriver.exe")
dr.get(url)
hd = dr.page_source


dr.close()


soup = BeautifulSoup(hd, "html.parser")

result = soup.select("#menuView2_632")
# name = result.find_all("caption")

for x in result:
    print(x.find_all("tr")[0].get_text())
    print()
    print(x.find_all("tr")[1].get_text())
    print()
    print(x.find_all("tr")[2].get_text())
# print(result)




# for x in result:
#     print(x.select(".center_t"))

