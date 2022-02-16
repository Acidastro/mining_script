import re
from typing import List

text = open('input.txt', 'r', encoding='utf8')
out = open('output2.txt', 'w', encoding='utf8')
z = []
for i in text.readlines():
    answer = (int((int(i.split()[-1]) + 100) * 0.1) + int(i.split()[-1]) + 100)
    if 'pieces' in i:  # есть ли pieces
        x = re.findall('[0-9]+', i)[-2]  # найти второе число с конца
        z = i.split()  # сделаем список из данной строки
        z.pop(z.index(x))  # удалим второе число с конца узнав его индекс
        z = i
        i = i[0:i.find('pieces')]  # вернуть без pieces
    elif 'Pieces' in i:
        x = re.findall('[0-9]+', i)[-2]  # найти второе число с конца
        z = i.split()  # сделаем список из данной строки
        z.pop(z.index(x))  # удалим второе число с конца узнав его индекс
        z = i
        i = i[0:i.find('Pieces')]  # вернуть без pieces
    elif 'pcs' in i:
        x = re.findall('[0-9]+', i)[-2]  # найти второе число с конца
        z = i.split()  # сделаем список из данной строки
        if 'pcs' in i.split():  # если pcs и число через пробел
            z.pop(z.index(x))  # удалим второе число с конца узнав его индекс
        else:  # если они написаны слитно
            z.pop(z.index(x + 'pcs'))  # удалим второе число с конца узнав его индекс
        z = i
        i = i[0:i.find('pcs')]  # вернуть без pieces
    elif 'tablets' in i:
        x = re.findall('[0-9]+', i)[-2]  # найти второе число с конца
        z = i.split()  # сделаем список из данной строки
        z.pop(z.index(x))  # удалим второе число с конца узнав его индекс
        z = i
        i = i[0:i.find('tablets')]  # вернуть без pieces
    elif 'slices' in i:
        x = re.findall('[0-9]+', i)[-2]  # найти второе число с конца
        z = i.split()  # сделаем список из данной строки
        z.pop(z.index(x))  # удалим второе число с конца узнав его индекс
        z = i
        i = i[0:i.find('slices')]  # вернуть без pieces

    # print(*i.split()[:-1], ',', answer, ',', int(answer/6.2), ',', int(answer*12.25), file=out)
    print(*i.split()[:-1], ',', answer, file=out)
    # print(*i.split()[:-1], ',', answer, ',', int(answer/6.2), ',', int(answer*12.25))
    print(*i.split()[:-1], answer)
