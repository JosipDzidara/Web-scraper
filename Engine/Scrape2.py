import requests
from bs4 import BeautifulSoup as bs
import inspect
from random import randint
from fake_useragent import UserAgent
import time
import re
import database

def get_data(n):
    for page in range(1,n):
        page_request = requests.get("https://www.njuskalo.hr/prodaja-kuca?page={}".format(page),headers = {"User-Agent":UserAgent().random})
        soup = bs(page_request.content,'html.parser')
        prices = soup.find_all("strong", attrs={"class":"price price--hrk"})
        areas =  soup.find_all("div",attrs={"class":"entity-description-main"})
        for i in range(len(prices)):
            price = prices[i].get_text().replace("kn",'').replace('.','').strip()
            area = areas[i].find(string=re.compile("Stambena"))
            if not area:
                break
            area = area.strip().replace("Stambena površina: ",'').replace(' m2','') 
            database.add_one(int(price),int(float(area)))


get_data(2)
