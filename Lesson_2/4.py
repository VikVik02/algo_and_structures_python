"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

def summa(k, n):
    if n > 1:
        return k + summa(k / (-2), n - 1)
    elif n == 1:
        return k

n = int(input("Введите количество элементов ряда"))
print(summa(1, n))