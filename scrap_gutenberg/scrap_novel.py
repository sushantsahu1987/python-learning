import os
import json
import requests

dirname = os.path.dirname(__file__)

def request_file(url):
    r = requests.get(url)
    return r.text

def write_text_to_file(file, content):
    filename = os.path.join(dirname, 'downloads/'+file+'.txt')
    f = open(filename,"w+")
    f.write(content)
    f.close()

def download():
    with open('novels_download_list.json') as json_file:
        data = json.load(json_file)
        for item in data:
            title = item['title'].strip()
            file = item['file'].strip()
            lower_case_title = ''.join(e for e in title if e.isalnum())
            lower_case_title = lower_case_title.lower()
            if not file.endswith('utf-8') and len(file) > 0:
                print(title)
                print(file)
                print(lower_case_title)
                print()
                respone = request_file('http://'+file);
                write_text_to_file(lower_case_title, respone)

download()