import requests
from bs4 import BeautifulSoup
import re
import json
from json import JSONEncoder

page = 1
offset = 24

url = 'http://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index='
url_list = []
catalogue_novel_urls_list = []

class Novel:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def display(self):
        return self.title + ' '+self.link


class NovelEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Novel):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

def print_list(list):
    for idx, item in enumerate(url_list):
        print("%d %s"%(idx, item))

def print_dictionary(dicts):
    for key, val in dicts.items():
        print(key,val)



while page < 1000:
    newurl = url + str(page)
    page = page + offset
    url_list.append(newurl)


def parse_web_page(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.text, 'xml')
    entries = soup.find_all("a", {"class": "link"})
    for idx, e in enumerate(entries):
        tags = e.find_all("span", {"class": "title"})
        title = tags[0].contents[0]
        value = e['href']
        if re.search("[0-9]$", value):
            n = Novel(title, 'http://www.gutenberg.org'+e['href'])
            catalogue_novel_urls_list.append(n)

for page in url_list:
    parse_web_page(page)

novellist_json = NovelEncoder().encode(catalogue_novel_urls_list)
f = open("catalogues.json","w+")
f.write(novellist_json)
f.close()