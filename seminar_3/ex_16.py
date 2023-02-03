'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''
import random
list = []
n = int(input('Input a number:'))   
for i in range(n):
    m = random.randint(1,10)
    list.append(m)
print(list)
x = int(input('Input x: ')) 
count = 0
for i in range(n):
    if list[i] == x:
        count += 1
print(count)        

