#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:16:42 2022

@author: acidastro
"""


from typing import List


def find_int(line):
    """Нахождение цены в конце строки и удаление лишнего после нее"""

    answer = ''
    for i in range(len(line)):  # перебираем все символы с конца
        if str(line[-1]).isdigit():  # как только нашли число
            while line[-1].isdigit():  # создаем цикл записи числа
                answer += line[-1]  # записываем
                line = line[:-1]  # и удаляем
            return ''.join(reversed(list(answer))), line  # возвращаем нужное число и строку отдельно
        else:
            line = line[:-1]  # если это не число, удаляем


def adding_a_percentage(answer):
    """Добавляем + 100 юаней и + 10% к нашему числу"""
    answer = int(answer)
    answer += 100
    answer *= 1.1
    return int(answer)


def filter(line):
    import re
    """
    Фильтруем строку, нужно убрать все упоминания о количестве
    (pcs,pieces,tablets,slices).
    """
    pattern = re.compile('pcs|pieces|tablets|slices')  # указываем паттерн для поиска
    if pattern.search(line):
        for i in range(len(line)):  # перебираем все символы с конца
            if str(line[-1]).isdigit():  # как только нашли число
                while line[-1].isdigit():  # создаем цикл удаления числа
                    line = line[:-1]  # и удаляем
                return line  # возвращаем строку
            else:
                line = line[:-1]  # если это не число, удаляем


text = open('input.txt', 'r', encoding='utf8')
out = open('output2.txt', 'w', encoding='utf8')
for i in text.readlines():
    answer, i = find_int(i)  # возвращаем итоговую цену и укороченую строку
    answer = adding_a_percentage(answer)  # добавляем процент
    i = filter(i).strip()
    print(i, answer)
