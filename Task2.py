# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
import math

n=int(input('Введите число: '))

def multiplicationSet(n):
    a=1
    while n>=a:
        print(math.factorial(a), end=', ')
        a+=1

multiplicationSet(n)