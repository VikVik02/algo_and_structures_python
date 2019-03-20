"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
n = int(input("Введите количество чисел"))
k = int(input("Введите номер простого числа"))

def resh(n, k):
    a = []
    for i in range(n + 1):
        a.append(i)
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return lst[k - 1]
# Сложность - О(n)

def without_resh(n, k):
    lst=[]
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[k - 1]
# Сложность - О(n^2)

print(resh(n, k))
print(without_resh(n, k))
print("Время с использованием решета Эратосфенаа", timeit.timeit("resh(n, k)", setup = 'from __main__ import resh, n, k', number = 1000))
print("Время без использования решета Эратосфена", timeit.timeit("without_resh(n, k)", setup = 'from __main__ import without_resh, n, k', number = 1000))

# Время с использованием решета Эратосфенаа 1.2184429569999997
# Время без использования решета Эратосфена 13.116453647
# (При n = 1000, k = 99)