#1
persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 45},
           {"name": "Van", "age": 53},
           {"name": "Alex", "age": 49},
           {"name": "Tom", "age": 15}
]
min_age = float('inf')
max_len = float('-inf')

for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
    if len(person['name']) > max_len:
        max_len = len(person['name'])


names_min_age = [i['name'] for i in persons if i['age'] == min_age]
names_max_len = [i['name'] for i in persons if len(i['name']) == max_len]

print(names_min_age)
print(names_max_len)
print(float(sum(d['age'] for d in persons)) / len(persons))
#2
def something(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    res = []
    for i in str1:
        if i in res:
            continue
        for k in str2:
            if i == k:
                res.append(i)
                break
    return res
print(something('some say the world will burn in fire','some say in ice'))

#3
def one_time(str1, str2):
    res = []
    for i in str1:
        j = str1.find(i) - str1.rfind(i)
        if j == 0:
            if i in str2 and str2.find(i) - str2.rfind(i) == 0:
                res.append(i)
    return res
print(one_time('some say the world will burn in fire','some say in ice'))
#4
from random import randint, choice
from exrex import getone

def create_email(domains, names):
    return f'{choice(names)}.{randint(100, 1000)}@{getone(r"[a-z]{5,7}")}.{choice(domains)}'

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)



