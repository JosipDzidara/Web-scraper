import json
import random
import requests
from bs4 import BeautifulSoup as bs
import inspect
from random import randint
from fake_useragent import UserAgent
from time import sleep
import re

data = {}


def get_data(n):
    for page in range(1,n):
        try:
            page_request = requests.get("https://www.njuskalo.hr/prodaja-kuca?page={}".format(page),headers = {"User-Agent":UserAgent().random})
            soup = bs(page_request.content,'html.parser')
            prices = soup.find_all("strong", attrs={"class":"price price--hrk"})
            areas =  soup.find_all("div",attrs={"class":"entity-description-main"})
            for i in range(len(prices)):
                price = prices[i].get_text().replace("kn",'').replace('.','').strip()
                price = int(price)
            
                loc = str(areas[i])
                loc = loc.split("</span>")[1].split(",")[0]
            
                area = areas[i].find(string=re.compile("Stambena"))
                area = area.strip().replace("Stambena površina: ",'').replace(' m2','') 
                area = float(area)
                data[str(i)] = {'price': price, 'location': loc, 'area': area}
            sleep(random.randint(4,10))
        except Exception:
            break
    with open('data.json', 'w+') as json_file:
        json.dump(data, json_file)



get_data(399)