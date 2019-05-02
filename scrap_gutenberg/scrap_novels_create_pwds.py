import requests
import random
from random import randint
import string
import passwordmeter

def random_number_genertator(size):
    return ''.join([random.choice(string.digits) for n in range(size)])


def random_special_chars_genertator(size):
    return ''.join([random.choice(['$','@','#','?','!']) for n in range(size)])

def words(w):
    w = w.replace('o','0')
    w = w.replace('a','@')
    return w


url = 'http://www.gutenberg.org/files/2701/2701-0.txt'
r = requests.get(url)
novel = r.text

lines = novel.splitlines()
items = []
size = 16

for l in lines:
    line = l.strip()
    line = l.capitalize()
    line = ''.join(e for e in line if e.isalnum())
    if len(line) > size:
        items.append(line)

max = len(items)
# print(max)
# for idx, item in enumerate(items):
#     print("%d %s"%(idx, item))

randum = randint(0,max)
pwd = items[randum]
pwd = pwd[0:size]
print(pwd)
pwd = pwd + random_number_genertator(4) +random_special_chars_genertator(1)
print(pwd)

strength, improvements = passwordmeter.test(pwd)

print(strength)

for key, value in improvements.items():
    print(key,":", value)