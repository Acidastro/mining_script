#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:16:42 2022

@author: acidastro
"""


from typing import List


def find_int(line):
    """
    Finding the price at the end of the string and removing the excess after it
    """
    answer = ''
    for i in range(len(line)):  # iterate over all characters from the end
        if str(line[-1]).isdigit():  # as soon as you find the number
            while line[-1].isdigit():  # create a loop for writing a number
                answer += line[-1]  # write down
                line = line[:-1]  # and delete
            return ''.join(reversed(list(answer))), line  # return the desired number and string separately
        else:
            line = line[:-1]  # if it's not a number, delete


def adding_a_percentage(answer):
    """
    Adding +100 yuan and +10% to our number
    """
    answer = int(answer)
    answer += 100
    answer *= 1.1
    return int(answer)


def filter(line):
    import re
    """
    We filter the line, we need to remove all references to the quantity
    (pcs,pieces,tablets,slices).
    """
    pattern = re.compile('pcs|pieces|tablets|slices')  # specify the search pattern
    if pattern.search(line.lower()):
        for i in range(len(line)):  # iterate over all characters from the end
            if str(line[-1]).isdigit():  # as soon as you find the number
                while line[-1].isdigit():  # create a deletion loop
                    line = line[:-1]  # and delete
                return line
            else:
                line = line[:-1]  # if it's not a number, delete


text = open('input.txt', 'r', encoding='utf8')
out = open('output2.txt', 'w', encoding='utf8')
for i in text.readlines():
    answer, i = find_int(i)  # return the total price and a shortened string
    answer = adding_a_percentage(answer)  # add percentage
    i = filter(i).strip()
    print(i, answer, file=out)
out.close()
text.close()
