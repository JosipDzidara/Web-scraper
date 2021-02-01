import json
import random
import requests
from bs4 import BeautifulSoup as bs
import inspect
from random import randint
from fake_useragent import UserAgent
from time import sleep
import re
import random


#Svaki user moze poslat maximum 5 req u minuti -> to znaci 1 req svakih 12 sekundi MINIMUM
#1 proxy maximum 500 requestova -> uzimamo 250 

class Scraper:
    def __init__(self) -> None:
        self.link: str = "https://www.njuskalo.hr/prodaja-kuca?page={}"
        self.address: str = "https://www.njuskalo.hr"
        self.list_of_links: list = []
        self.counter: int = 0
        self.data = {'Lokacija': '0','Cijena':'0','Broj soba': '0', 'Stambena površina': '0', 'Površina okućnice': '0', 'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
        self.dataset: dict = {}
        self.index: str = ""
        self.proxy: dict = self.give_proxy()
                            	
                            	
    def give_proxy(self):
        my_file = open("Engine\proxies.txt", "r")
        content = my_file. read()
        content_list = content. split("\n")
        my_file. close()
        proxy = {
                    "http": "https://{}".format(random.choice(content_list))
                }
        return proxy

    def render_html(self,element):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr, '', str(element))

    def start_scraper(self, a, n):
        for page in range(a, n):
            sleep(random.randint(2,6))
            print("You are currently on page {}".format(page))
            if self.counter%250 == 0:      #Maximum 250 requestova
                self.proxy = self.give_proxy()
            page_request = requests.get(self.link.format(page), headers = {"User-Agent":UserAgent().random},proxies = self.proxy) 
            soup = bs(page_request.content,'html.parser')
            #filename = "njuskalo-{}.html".format(page)        #Da vidimo sta dobije ->
            #with open(filename, 'w+',encoding='utf-8') as f:
            #    f.write(str(soup))                            #                     <-
            self.get_links(soup, page,n)
            self.get_data()
            self.list_of_links = []   #!Error :set back to empyt 
            sleep(random.randint(10,20))

    def get_links(self, soup, page,n):
        cleanr = re.compile('<.*?>')
        try:
            self.index = soup.select("#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > header > div.entity-list-meta > strong")
            self.index = re.sub(cleanr, '', str(self.index[0])) 
        except Exception:
            if soup.find_all("div",attrs={"class":"captcha-mid"}):
                print("Fail")
                sleep(randint(20,40))
                page = page + 1
            else:
                page = page
            sleep(randint(3,7))
            self.start_scraper(a=page, n=n)
        if self.index:
            parent = soup.select("#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > div.EntityList.EntityList--Standard.EntityList--Regular.EntityList--ListItemRegularAd.EntityList--itemCount_{} > ul > li > article > h3 > a".format(self.index))
            if not parent:
                page = page
                sleep(randint(10,20))
                self.start_scraper(a=page, n=n)
            for link in parent:
                self.list_of_links.append(self.address + link.get('href'))
    
    def get_data(self):
        with open('data3.json', 'a+') as json_file:
            for link in self.list_of_links:
                self.data = {'Lokacija': '0', 'Broj soba': '0', 'Stambena površina': '0', 'Površina okućnice': '0', 'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
                self.counter += 1
                page_request = requests.get(link, headers = {"User-Agent":UserAgent().random},proxies = self.proxy)
                sleep(randint(12,20))
                soup = bs(page_request.content,'html.parser')
                table_data = list(soup.select("#content-main > div.content-primary > div > div.content-main > div.BlockStandard.ClassifiedDetailBasicDetails span"))
                price = soup.select("#content-main > div.content-primary > div > div.content-main > div:nth-child(3) > div.ClassifiedDetailSummary.cf > div.ClassifiedDetailSummary-topControls.cf > div.ClassifiedDetailSummary-pricesBlock > dl > dd")                
                if not table_data and not price:
                    sleep(randint(12,20))
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
scraper.start_scraper(2,4)

