'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count
from itertools import cycle

# Задание а)

# print([itm for itm in count(115) if itm <= 130]) # Не понимаю, почему эта конструкция не работает.

for itm in count(115):
    if itm > 130:
        break
    else:
        print(itm)

# Задание б)

special_list = 'Карл у Клары украл кораллы'
i = 0
for itm in cycle(special_list.split(' ')):
    print(itm)
    i += 1
    if i > 30:
        break