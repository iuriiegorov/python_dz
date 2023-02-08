'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12'''

import random
lst1 = []
n = int(input('Enter n: '))   
for i in range(n):
    k = random.randint(1,20)
    lst1.append(k)
print(lst1)
lst2 = []
m = int(input('Enter m: '))   
for i in range(m):
    q = random.randint(1,20)
    lst2.append(q)
print(lst2)
a = set(lst1)
b = set(lst2)
z = list(a.intersection(b))
print (sorted(z))