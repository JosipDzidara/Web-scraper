import json
import random
import requests
from bs4 import BeautifulSoup as bs
import inspect
from random import randint
from fake_useragent import UserAgent
from time import sleep
import re

class Scraper:
    def __init__(self, n) -> None:
        self.link: str = "https://www.njuskalo.hr/prodaja-kuca?page={}"
        self.address: str = "https://www.njuskalo.hr"
        self.number_of_pages: range = range(1, n)
        self.list_of_links: list = []
        self.counter: int = 0
        self.data = {'Lokacija': '0', 'Broj soba': '0', 'Stambena površina': '0', 'Površina okućnice': '0', 'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
        self.dataset: dict = {}
        self.index: str = ""



    def send_requests(self, n):
        for page in self.number_of_pages:
            print("You are currently on page {} out of {}".format(page, n))
            page_request = requests.get(self.link.format(page), headers = {"User-Agent":UserAgent().random})
            soup = bs(page_request.content,'html.parser')
            self.get_links(soup)
            self.get_data()
            sleep(random.randint(2,6))
        self.save_data_to_json()

    def get_links(self, soup):
        if not self.index:
            self.index = str(soup.select("#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > header > div.entity-list-meta > strong")).split(">")[1].split("<")[0]
        parent = soup.select("#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > div.EntityList.EntityList--Standard.EntityList--Regular.EntityList--ListItemRegularAd.EntityList--itemCount_{} > ul > li > article > h3 > a".format(parent_var))
        for link in parent:
            self.list_of_links.append(self.address + link.get('href'))
    
    def get_data(self):
        for link in self.list_of_links:
            self.counter += 1
            page_request = requests.get(link, headers = {"User-Agent":UserAgent().random})
            sleep(randint(2,5))
            soup = bs(page_request.content,'html.parser')
            table_data = list(soup.select("#content-main > div.content-primary > div > div.content-main > div.BlockStandard.ClassifiedDetailBasicDetails span"))
            for element in range(0, len(table_data), 2):
                cleanr = re.compile('<.*?>')
                cleantext_1 = re.sub(cleanr, '', str(table_data[element]))
                cleantext_2 = re.sub(cleanr, '', str(table_data[element+1]))
                if cleantext_1 in self.data.keys():
                    self.data[cleantext_1] = cleantext_2
                    self.dataset[self.counter] = self.data
    
    def save_data_to_json(self):
        with open('data.json', 'w+') as json_file:
            json.dump(self.dataset, json_file)

scraper = Scraper(2)
scraper.send_requests(2)

