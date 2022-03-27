# Task 1
"""Написать функцию num_translate(), переводящую числительные от 0 до 10
c английского на русский язык."""

nums = {'zero': 'ноль', 'one': 'один', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
        'nine': 'девять', 'ten': 'десять'}


def num_translate(key):
    print(f'{nums.get(key)}')


num_translate('zero')
num_translate('one')
num_translate('ten')
num_translate('five')
num_translate('qwe')

# Task 2
"""*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
реализовать корректную работу с числительными, начинающимися с заглавной буквы
 — результат тоже должен быть с заглавной."""


def num_translate_adv(key):
    if key.istitle():
        key = key.lower()
        if nums.get(key) is None:
            print('None')
        else:
            print(nums.get(key).title())
    else:
        print(nums.get(key))


num_translate_adv('zero')
num_translate_adv('Seven')
num_translate_adv('Qwe')
num_translate_adv('qwe')

# Task 3
"""Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
 и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
  содержащие имена, начинающиеся с соответствующей буквы."""


def thesaurus(*args):
    names = {}
    for name in args:
        names.setdefault(name[0], [])
        names[name[0]].append(name)

    return print(names)


thesaurus('Иван', 'Мария', 'Петр', 'Илья')

# Task 4
"""Не сделал, так как для меня было достаточно сложно, а просто копировать Ваш код из проверки не стал"""

# Task 5
"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
 взятых из трёх списков (по одному из каждого)"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    result = []
    i = 0
    while i < num:
        word1 = (random.choice(nouns))
        word2 = (random.choice(adverbs))
        word3 = (random.choice(adjectives))
        words = [word1 + ' ' + word2 + ' ' + word3]
        result.append(words)
        i += 1
    return result


print(get_jokes(2))
print(get_jokes(3))
