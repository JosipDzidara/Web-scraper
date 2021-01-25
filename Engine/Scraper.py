from urllib.request import urlopen
from bs4 import BeautifulSoup

LINK = ''
def return_page_title(LINK):
    page_link = urlopen(LINK).read()
    soup = BeautifulSoup(page_link, 'html.parser')
    return soup.title.string



