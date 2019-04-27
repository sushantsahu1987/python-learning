import requests
from bs4 import BeautifulSoup
import hashlib

def writetofile(entry):
    f = open('summary.html','w')
    f.write(entry.summary.text)
    f.close()

url = 'https://openbanking.atlassian.net/wiki/createrssfeed.action?types=page&pageSubTypes=comment&pageSubTypes=attachment&types=blogpost&blogpostSubTypes=comment&blogpostSubTypes=attachment&spaces=conf_all&title=Confluence+RSS+Feed&labelString%3D&excludedSpaceKeys%3D&sort=modified&maxResults=10&timeSpan=5&showContent=true&confirm=Create+RSS+Feed&os_authType=basic'
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text,'xml')
# print(soup.prettify())
entries = soup.findAll('entry')
# print(len(entries))

for entry in entries:
    text = entry.title.contents[0]
    # print(text)
    # print(text.find('API Downtime'))
    if text.find('API Downtime') >= 0 :
        summary = entry.summary.text
        html = BeautifulSoup(summary,'lxml')
        # css_soup.p['class']
        trs = html.find_all('tr')
        for tr in trs:
            tds = tr.findAll('td')
            if len(tds) > 0:
                print(tds[5].contents[0])
                print(tds[6].contents[0])
                print(tds[8].contents[0])
            print('\n')
