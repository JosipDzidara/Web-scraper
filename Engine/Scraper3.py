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


def get_data(n):
    data = {}
    count = 1
    for page in range(1,n):
        print("Trenutno sam na obradi stranice {}".format(page))
        #try:
        page_request = requests.get("https://www.njuskalo.hr/prodaja-kuca?page={}".format(page),headers = {"User-Agent":UserAgent().random})
        soup = bs(page_request.content,'html.parser')
        items = soup.find_all("ul",attrs={"class":"EntityList-items"})
        print(items)


get_data(2)