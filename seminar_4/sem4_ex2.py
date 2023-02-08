'''Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
4
1 2 3 4
9'''

import random
rlst = []
for i in range(random.randint(3,10)):
    n = random.randint(1,10)
    rlst.append(n)
print(rlst)
result = rlst[-3] + rlst[-2] + rlst[-1]
for i in range(0,len(rlst)):
    if rlst[i-2] + rlst[i-1] + rlst[i] > result:
        result = rlst[i-2] + rlst[i-1] + rlst[i]
print(result)        