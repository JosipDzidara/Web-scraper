from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from fake_useragent import UserAgent

import requests
from requests import utils

# LINK = input('')
# def return_page_title(LINK):
#     page_link = urlopen(LINK).read()
#     soup = BeautifulSoup(page_link, 'html.parser')
#     return soup.title.string

def return_data_from_a_website():
    title = []
    price = []
    sqm = []
    location = []

    ua = UserAgent()
    pages = range(1,11)
    headers = utils.default_headers()
    headers.update({'User-Agent': ua.ie})

    for page in pages:
        page_request = requests.get("https://www.njuskalo.hr/prodaja-kuca?page={}".format(page), headers)
        soup = BeautifulSoup(page_request.text, 'html.parser')
        filename = "njuskalo-{}.html".format(page)
        with open(filename, 'a+') as f:
            f.write(str(soup))
        sleep(randint(2,10))

return_data_from_a_website()





