'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random
rlst = []
for i in range(random.randint(5,20)):
    n = random.randint(1,100)
    rlst.append(n)
print(rlst)
mi = int(input('Input minimum:'))
ma = int(input('Input maximum:'))
for i in range(len(rlst)):
   if rlst[i] >= mi and rlst[i] <= ma:
       print(i)
