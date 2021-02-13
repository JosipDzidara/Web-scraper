import json
import requests
from bs4 import BeautifulSoup as bs
from random import randint
from fake_useragent import UserAgent
from time import sleep
import re
import random


class Scraper:
    def __init__(self) -> None:
        self.link: str = "https://www.njuskalo.hr/prodaja-kuca?page={}"
        self.address: str = "https://www.njuskalo.hr"
        self.list_of_links: list = []
        self.counter: int = 3222
        self.data = {'Lokacija': '0', 'Cijena': '0', 'Broj soba': '0', 'Stambena površina': '0',
                     'Površina okućnice': '0', 'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
        self.dataset: dict = {}
        self.index: str = ""

    def start_scraper(self, begin, end):
        for page in range(begin, end):
            sleep(random.randint(20, 40))
            print("You are currently on page {}".format(page))
            # print(self.proxy)
            # if self.counter%250 == 0:
            #    self.proxy = self.give_proxy()
            page_request = requests.get(self.link.format(page), headers={"User-Agent": UserAgent().random})
            soup = bs(page_request.content, 'html.parser')
            self.get_individual_links(soup, page, end)
            self.get_data()
            self.list_of_links = []
            with open('../Model/raw_data.json', 'a+') as json_file:
                json.dump(self.dataset, json_file)
            self.dataset = {}
            sleep(random.randint(1, 2))

    def get_individual_links(self, soup, page, n):
        cleanr = re.compile('<.*?>')
        try:
            self.index = soup.select(
                "#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > "
                "header > div.entity-list-meta > strong")
            self.index = re.sub(cleanr, '', str(self.index[0]))
        except Exception:
            if soup.find_all("div", attrs={"class": "captcha-mid"}):
                print("Captcha discovered!")
                raise ValueError
            else:
                sleep(random.randint(8, 10))
                self.start_scraper(page, n)

        if self.index:
            parent = soup.select(
                "#form_browse_detailed_search > div > div.content-main > div.block-standard.block-standard--epsilon > "
                "div.EntityList.EntityList--Standard.EntityList--Regular.EntityList--ListItemRegularAd.EntityList"
                "--itemCount_{} > ul > li > article > h3 > a".format(
                    self.index))
            for link in parent:
                self.list_of_links.append(self.address + link.get('href'))

    def get_clean_string(self, element) -> str:
        cleaner = re.compile('<.*?>')
        cleaned_string = re.sub(cleaner, '', str(element))
        return cleaned_string

    def get_data(self):
        for link in self.list_of_links:
            sleep(random.randint(7, 9))
            self.data = {'Lokacija': '0', 'Broj soba': '0', 'Stambena površina': '0', 'Površina okućnice': '0',
                         'Broj parkirnih mjesta': '0', 'Pogled na more': '0'}
            self.counter += 1
            page_request = requests.get(link, headers={"User-Agent": UserAgent().random})
            sleep(randint(8, 12))
            soup = bs(page_request.content, 'html.parser')
            try:
                self.get_price(soup)
            except IndexError:
                continue
            table_data = list(soup.select(
                "#content-main > div.content-primary > div > div.content-main > "
                "div.BlockStandard.ClassifiedDetailBasicDetails span"))
            if not table_data:
                sleep(randint(1, 2))
                self.counter -= 1
                continue
            self.get_property_data(table_data)

    def get_price(self, soup):
        price = soup.select(
            "#content-main > div.content-primary > div > div.content-main > div:nth-child(3) > "
            "div.ClassifiedDetailSummary.cf > div.ClassifiedDetailSummary-topControls.cf > "
            "div.ClassifiedDetailSummary-pricesBlock > dl > dd")
        price = self.get_clean_string(price).split()[1]
        self.data['Cijena'] = price

    def get_property_data(self, table_data):
        for element in range(0, len(table_data), 2):
            cleantext_1 = self.get_clean_string(table_data[element])
            cleantext_2 = self.get_clean_string(table_data[element + 1])
            if cleantext_1 == 'Lokacija':
                cleantext_2 = cleantext_2.split(',')[0]
            if cleantext_1 in self.data.keys():
                self.data[cleantext_1] = cleantext_2
                self.dataset[self.counter] = self.data
