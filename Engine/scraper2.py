import json
import random
import requests
from bs4 import BeautifulSoup as bs
import inspect
from random import randint
from fake_useragent import UserAgent
from time import sleep
import re
from selenium import webdriver


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = re.split("\s{3,}",cleantext)
  cleantext.pop(0)
  cleantext.pop()
  clean_dict = {}
  for i in range(0,int(len(cleantext)),2):
      clean_dict[cleantext[i]] = cleantext[i+1]
  return clean_dict




def get_data(n):
    data = {}
    count = 1
    for page in range(1,n):
        print("Trenutno sam na obradi stranice {}".format(page))
        #try:
        page_request = requests.get("https://www.njuskalo.hr/prodaja-kuca?page={}".format(page),headers = {"User-Agent":UserAgent().random})
        soup = bs(page_request.content,'html.parser')
        items = soup.find_all("h3",attrs={"class":"entity-title"})
        link_new = "https://www.njuskalo.hr" + str(items[1]).split('href=')[1].split('name')[0].replace("\"","")
        print(link_new)
        page_request = requests.get(link_new,headers = {"User-Agent":UserAgent().random})
        sleep(random.randint(5,10))
        soup = bs(page_request.content,'html.parser')
        table_raw = str(soup.find_all('div',attrs={"class":"BlockStandard ClassifiedDetailBasicDetails"}))
        print(table_raw)
        table = cleanhtml(table_raw)
        print(table)
            #filename = "njuskalo5.html"
            #with open(filename, 'w+',encoding='utf-8') as f:
            #    f.write(str(soup))
        #except Exception: 
            #print("Uhvacen sam")
            #break


#string=re.compile("(H|h)eader")
#headers = soup.find_all("h2",string=re.compile("(H|h)eader"))
get_data(2)

#ul class="EntityList-items"