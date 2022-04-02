# Task 1
"""Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield"""


def odd_gen(num):
    for num in range(1, num + 1, 2):
        yield num


num15 = odd_gen(15)
print(odd_gen(15))
print(next(num15))
print(next(num15))
print(next(num15))
print(next(num15))
print(next(num15))
print(next(num15))
print(next(num15))
print(next(num15))

# Task 2
"""Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield"""
num15 = (num for num in range(1, 15 + 1, 2))

print(*num15)

# Task 3
"""Есть два списка: Необходимо реализовать генератор, возвращающий кортежи вида
(<tutor>, <klass>)
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors,
необходимо вывести последние кортежи в виде: (<tutor>, None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект."""

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


tuple_gen = ((row1, row2) for row1, row2 in zip_longest(tutors, klasses, fillvalue=None) if row1 is not None)


print(*tuple_gen)

# Task 4
"""Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего"""


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


result = [num1 for num1, num2 in zip(src[1:], src[:-1]) if num1 > num2]
print(result)

# Task 5
"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования
в исходном списке"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [num for num in src if src.count(num) == 1]

print(result)

