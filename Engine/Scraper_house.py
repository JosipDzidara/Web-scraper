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
    def __init__(self) -> None:
        self.link: str = "https://www.njuskalo.hr/prodaja-kuca?page={}"
        self.address: str = "https://www.njuskalo.hr"
        self.list_of_links: list = []
        self.counter: int = 0
        self.data = {'Lokacija': '0','Cijena':'0','Broj soba': '0', 'Stambena površina': '0', 'Površina okućnice': '0', 'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
        self.dataset: dict = {}
        self.index: str = ""


    def render_html(self,element):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr, '', str(element))

    def start_scraper(self, a, n):
        for page in range(a, n):
            print("You are currently on page {}".format(page))
            page_request = requests.get(self.link.format(page), headers = {"User-Agent":UserAgent().random})
            soup = bs(page_request.content,'html.parser')
            self.get_links(soup, page)
            self.get_data()
            sleep(random.randint(2,6))

    def get_links(self, soup, page):
        cleanr = re.compile('<.*?>')
        self.index = soup.select("#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > header > div.entity-list-meta > strong")
        if not self.index:
            page = page
            sleep(3)
            self.start_scraper(a=page, n=2)
        self.index = re.sub(cleanr, '', str(self.index[0])) 
        parent = soup.select("#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > div.EntityList.EntityList--Standard.EntityList--Regular.EntityList--ListItemRegularAd.EntityList--itemCount_{} > ul > li > article > h3 > a".format(self.index))
        if not parent:
            page = page
            sleep(3)
            self.start_scraper(a=page, n=400)
        for link in parent:
            self.list_of_links.append(self.address + link.get('href'))
    
    def get_data(self):
        with open('data.json', 'w+') as json_file:
            for link in self.list_of_links:
                self.data = {'Lokacija': '0', 'Broj soba': '0', 'Stambena površina': '0', 'Površina okućnice': '0', 'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
                self.counter += 1
                page_request = requests.get(link, headers = {"User-Agent":UserAgent().random})
                sleep(randint(2,5))
                soup = bs(page_request.content,'html.parser')
                table_data = list(soup.select("#content-main > div.content-primary > div > div.content-main > div.BlockStandard.ClassifiedDetailBasicDetails span"))
                price = soup.select("#content-main > div.content-primary > div > div.content-main > div:nth-child(3) > div.ClassifiedDetailSummary.cf > div.ClassifiedDetailSummary-topControls.cf > div.ClassifiedDetailSummary-pricesBlock > dl > dd")                
                if not table_data and not price:
                    sleep(5)
                    continue
                price = self.render_html(price).split()[1]
                self.data['Cijena'] = price
                for element in range(0, len(table_data), 2):
                    cleanr = re.compile('<.*?>')
                    cleantext_1 = re.sub(cleanr, '', str(table_data[element]))
                    cleantext_2 = re.sub(cleanr, '', str(table_data[element+1]))
                    if cleantext_1 == 'Lokacija':
                        cleantext_2 = cleantext_2.split(',')[0]
                    if cleantext_1 in self.data.keys():
                        self.data[cleantext_1] = cleantext_2
                        self.dataset[self.counter] = self.data                
            json.dump(self.dataset, json_file)

scraper = Scraper()
scraper.start_scraper(1,2)

