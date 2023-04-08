# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import json
import csv
import random
from typing import Callable

file = 'home9.csv'
json_file = 'home9.json'


def deco_scv(func: Callable, csv_file=file):
    result = []
    argument = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        while data := f.readline()[:-1]:
            argument.append(data)

    def wrapper():
        for i in argument:
            temp = i.split(',')
            result.append(func(int(temp[0]), int(temp[1]), int(temp[2])))
        return result

    return wrapper


def deco_json(func: Callable, json_f=json_file):
    result = {}

    def wrapper(*args):
        with open(json_f, 'w', encoding='utf-8') as j:
            res = func(*args)
            string = ''
            for i in args:
                string += str(i) + ","
            result[string] = res
            json.dump(result, j, indent=2)
        return None

    return wrapper


@deco_scv
@deco_json
def roots_quadratic_equation(a: int, b: int, c: int) -> list[complex | float]:
    list_ = []
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b - d ** 0.5) / (2 * a)
        x2 = (- b + d ** 0.5) / (2 * a)
        list_.append(x1)
        list_.append(x2)
    elif d == 0:
        x = - b / (2 * a)
        list_.append(x)
    else:
        d: complex = complex(d)
        x1 = (- b - d ** 0.5) / (2 * a)
        x2 = (- b + d ** 0.5) / (2 * a)
        list_.append(str(x1))
        list_.append(str(x2))
    return list_


def csv_generator(string_count: int, csv_file: str, max_: int = 100) -> None:
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        for i in range(string_count):
            (a, b, c) = random.randint(1, max_), random.randint(1, max_), random.randint(1, max_)
            csv_write = csv.writer(f, dialect='excel')
            csv_write.writerow((a, b, c))


if __name__ == '__main__':
    # csv_generator(100, file)
    roots_quadratic_equation()
