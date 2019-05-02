import json
import requests
from bs4 import BeautifulSoup
from json import JSONEncoder

class Novel:
    def __init__(self, title, file):
        self.title = title
        self.file = file

    def display(self):
        return self.title + ' '+self.file


class NovelEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Novel):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

novels_list = []

def parse_web_page(link):
    bookurl = ''
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'xml')
    entries = soup.find_all("a", {"class": "link"})
    # print(len(entries))
    for idx, e in enumerate(entries):
        if len(e.contents) > 0 and e.contents[0] == 'Plain Text UTF-8':
            bookurl = e['href'].strip()
            bookurl = bookurl[2: len(bookurl)]
            # print(bookurl)
    return bookurl

with open('catalogues.json') as json_file:
    data = json.load(json_file)
    for item in data:
        title = item['title'].strip()
        link = item['link'].strip()
        print(title, link)
        bookurl = parse_web_page(link)
        n = Novel(title, bookurl)
        novels_list.append(n)


for n in novels_list:
    print(n.display())

novellist_json = NovelEncoder().encode(novels_list)
f = open("novels_download_list.json","w+")
f.write(novellist_json)
f.close()
