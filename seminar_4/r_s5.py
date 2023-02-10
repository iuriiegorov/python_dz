'''Напишите функцию, которая принимает одно число и проверяет, является ли оно простым'''
def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True    
n = int(input('--> '))
print(prime(n))