# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n=str(input('Введите число: '))

def ost(x):
    x=x.replace('-', '')
    x=int(x.replace('.', ''))

    while x<1:
        x*=10
    
    sum=0
    while x>0:
        a=x%10
        sum+=a
        x=x//10
    return sum
    
print(ost(n))