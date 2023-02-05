#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
xlist = []
for i in range(random.randint(1,10)):
    n = round(random.uniform(0, 10), 2)
    xlist.append(n)
print(xlist)
ylist = []
for i in range(len(xlist)):
    ylist.append(round(xlist[i]*100%100))
print('Max - Min: ', max(ylist) - min(ylist))