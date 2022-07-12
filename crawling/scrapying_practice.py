import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%B7"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

data = soup.select(".list_vertical")

print(data)


for idx, x in enumerate(data):
    img_url = x.find("img")["src"]
    img_res = requests.get(img_url)
    img_res.raise_for_status()

    with open(f"mo_thumb_{idx}.jpg","wb") as f:
        f.write(img_res.content)