# Task 1
"""Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)"""
from requests import get

r = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text = r.text
with open('text.txt', 'w+') as f:
    f.write(text)
with open('text.txt', 'r') as f:
    f = f.read()
f = f.split('"')

l_vt = []
for i in f:
    if '- -' in i:
        l_vt.append(i[1:13])

l_vue = []
for i in f:
    if 'GET' in i:
        l_vue.append(i[0:24])

ln = []
for items in (zip(l_vt, l_vue)):
    ln.append(items)

print(ln)

# Task 3
"""Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ."""

with open('users.txt') as f:
    names = f.read().splitlines()

with open('hobby.txt') as f:
    hobby = f.read().splitlines()

din = dict(zip(names, hobby))

with open('dict.txt', 'w+') as f:
    f.write(str(din))

# Task 4
"""Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Только теперь не нужно создавать словарь с данными.
Вместо этого нужно сохранить объединенные данные в новый файл
(users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО"""

from itertools import zip_longest

with open('users.txt', ) as f:
    names = f.read().splitlines()

    names1 = []
    for i in names:
        i = i.replace(',', ' ')
        names1.append(i)

with open('hobby.txt') as f:
    hobby = f.read().splitlines()

with open('users_hobby.txt', 'w+') as f:
    for k, j in zip_longest(names1, hobby):
        f.write(f'{k}: {j}\n')

if len(names1) < len(hobby):
    exit(1)
