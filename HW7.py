# Task 1
"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp """
import os

dir_name = 'my_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

os.chdir('/Users/amerekin/PycharmProjects/pythonGB/HW7/my_project')
file_name1 = open('settings', 'w')
file_name2 = open('mainapp', 'w')
file_name3 = open('adminapp', 'w')
file_name4 = open('authapp', 'w')
file_name1.close()
file_name2.close()
file_name3.close()
file_name4.close()


# Task 3
"""Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates,
например:
|--my_project
...
    |--templates
        |--mainapp
            |--base.html
            |--index.html
        |--authapp
            |--base.html
            |--index.html"""

import os
import shutil

dir_name = 'new_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

folder = 'my_project'
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(dir_name, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)

# Task 4
"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
а значения — общее количество файлов (в том числе и в подпапках), размер которых 
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
    out_dict[10 ** len(str(file))] += 1


print(out_dict)