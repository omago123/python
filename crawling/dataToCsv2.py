import csv
import requests
from bs4 import BeautifulSoup

# 데이터를 추출해서 csv로 만들 url
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"

fName = "test1.csv"
f = open(fName,"w",encoding="utf-8-sig", newline="")
writer = csv.writer()

