"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from memory_profiler import profile

@profile
def func():
    a = list(range(50000))

    max_a = a[0]
    min_a = a[0]

    min_index = 0
    for i in range(len(a)):
        if min_a > a[i]:
            min_a = a[i]
            min_index = i
    print("Минимальный элемент: ", min_a)

    max_index = 0
    for i in range(len(a)):
        if max_a < a[i]:
            max_a = a[i]
            max_index = i
    print("Максимальный элемент: ", max_a)

    summ = 0

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    for i in range(min_index + 1, max_index):
        summ += a[i]

    print(f"Сумма между минимальным и максимальным элементом массива {summ}")
    del a

if __name__== "__main__":
    func()

'''
16.1 MiB - Для запуска программы.
0.9 MiB - на создание списка а.
После удаления списка "a" освободилось 0.7 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
     8     16.1 MiB     16.1 MiB   @profile
     9                             def func():
    10     17.0 MiB      0.9 MiB       a = list(range(50000))
    11
    12     17.0 MiB      0.0 MiB       max_a = a[0]
    13     17.0 MiB      0.0 MiB       min_a = a[0]
    14
    15     17.0 MiB      0.0 MiB       min_index = 0
    16     17.0 MiB      0.0 MiB       for i in range(len(a)):
    17     17.0 MiB      0.0 MiB           if min_a > a[i]:
    18                                         min_a = a[i]
    19                                         min_index = i
    20     17.0 MiB      0.0 MiB       print("Минимальный элемент: ", min_a)
    21
    22     17.0 MiB      0.0 MiB       max_index = 0
    23     17.1 MiB      0.0 MiB       for i in range(len(a)):
    24     17.1 MiB      0.0 MiB           if max_a < a[i]:
    25     17.1 MiB      0.0 MiB               max_a = a[i]
    26     17.1 MiB      0.0 MiB               max_index = i
    27     17.1 MiB      0.0 MiB       print("Максимальный элемент: ", max_a)
    28
    29     17.1 MiB      0.0 MiB       summ = 0
    30
    31     17.1 MiB      0.0 MiB       if min_index > max_index:
    32                                     min_index, max_index = max_index, min_index
    33
    34     17.1 MiB      0.0 MiB       for i in range(min_index + 1, max_index):
    35     17.1 MiB      0.0 MiB           summ += a[i]
    36
    37     17.0 MiB      0.0 MiB       print(f"Сумма между минимальным и максимальным элементом массива {summ}")
    38     16.3 MiB      0.0 MiB       del a
'''