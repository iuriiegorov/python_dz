'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
'''

import random
list = []
n = int(input('Input a number: '))   
for i in range(n):
    m = random.randint(1,10)
    list.append(m)
print(list)
x = int(input('Input a number: '))  
y = x
near = list[0]
for i in list:
    if abs(i - x) < y:
        y = abs(i - x)
        near = i
print(near)
