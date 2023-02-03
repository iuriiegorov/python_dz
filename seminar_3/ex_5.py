#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Input a number: '))
f = -1
f1 = 1
list = []
for i in range(n-1):
    f , f1 = f1 , f - f1
    list.append(-f)
list.reverse()
f0 = 0
f2 = 1
list.append(f0)
for i in range(n):
    f0 , f2 = f2 , f2 +f0
    list.append(f0)
print(list)