#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#стоящих на нечётной позиции.
#Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
rlst = []
for i in range(random.randint(1,10)):
    n = random.randint(1,10)
    rlst.append(n)
print(rlst)
sum = 0
for i in range(len(rlst)):
    if i%2 != 0:
        sum +=rlst[i]
print(sum)