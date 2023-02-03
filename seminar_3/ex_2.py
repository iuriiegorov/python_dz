#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
#второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import random
randomlist = []
for i in range(random.randint(1,10)):
    n = random.randint(1,10)
    randomlist.append(n)
print(randomlist)

if (len(randomlist)%2 == 0):
    for i in range(int(len(randomlist)/2)):
        print(randomlist[i]*randomlist[len(randomlist) -i -1])
else:
     for i in range(int(len(randomlist)/2 + 1)):
        print(randomlist[i]*randomlist[len(randomlist) -i -1])