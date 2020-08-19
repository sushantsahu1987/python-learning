import os
from random import randint
import random
import string
import passwordmeter
import json

dirname = os.path.dirname(__file__)
paths = os.path.join(dirname, 'downloads')
file_list = []
lines = []

for file in os.listdir(paths):
    filename = os.path.join(dirname, 'downloads/'+file)
    file_list.append(filename)

file_start = 0
file_max = len(file_list)
rand_num = randint(file_start,file_max)

print(file_max, rand_num)
file = file_list[rand_num]
print(file)

def random_number_genertator(size):
    return ''.join([random.choice(string.digits) for n in range(size)])


def random_special_chars_genertator(size):
    return ''.join([random.choice(['$','@','#','?','!']) for n in range(size)])

f = open(file)
for line in f:
    l = line.strip()
    l = l.split('.')
    if len(l) > 1:
        for item in l:
            words = item.strip()
            words = words.lower()
            words_size = len(words.split(' '))
            if words_size > 2:
                sentence = words.split(' ')
                s = ''
                i = 0
                while i < len(sentence):
                    if i == 0:
                        s = s + sentence[i].upper() + ' '
                    else:
                        s = s + sentence[i]+ ' '
                    i+=1
                s = ''.join(e for e in s if e.isalnum())
                lines.append(s+ random_number_genertator(4) + random_special_chars_genertator(1))
f.close()


# print(len(lines))
line_random = randint(0,len(lines))
# for idx, l in enumerate(lines):
#     print(idx, l)

w = lines[line_random]
strength, improvements = passwordmeter.test(w)

password = {
    "password": w,
    "strength": strength,
    "improvements": improvements
}

password_json = json.dumps(password)

print(password_json)

