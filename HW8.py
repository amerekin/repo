# Task 1
"""Написать функцию email_parse(<email_address>), которая
при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError."""

import re

pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

RE_EMAIL = re.compile(pattern)


def email_parse(email):
    name_domain_keys = ('username', 'domain')
    if not RE_EMAIL.match(email):
        raise ValueError
    else:
        email = email.split('@')
        name_domain_dict = dict(zip(name_domain_keys, email))
    return name_domain_dict


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someonegeekbrains.ru'))

# Task 3
"""Написать декоратор для логирования типов позиционных аргументов функции"""

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(args):
        print(f'{func(args)} {type(args)}')
        return func(args)

    return wrapper


@type_logger
def calc_cube(x):
    """func to calculate x ** 3"""
    return x ** 3


calc_cube(10)
print(calc_cube.__doc__)
print(calc_cube.__name__)
