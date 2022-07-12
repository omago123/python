import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

myData = soup.find_all("ol")

print(len(myData))

result = myData[1].select("li")
# print(result)

for x in result:
    print(x["class"][0])
    print(x.select("a")[0]["title"])
