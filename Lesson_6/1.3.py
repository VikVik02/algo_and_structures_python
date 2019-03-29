#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from memory_profiler import profile

@profile
def func():
    a = list(range(100000))

    max_neg_elem = a[0]
    pos = 0
    for i in range(len(a)):
        if a[i] < 0:
            if max_neg_elem < a[i]:
                max_neg_elem = a[i]
                pos = i

    print(f"Максимальный отрицательный элемент в массиве: {max_neg_elem}")
    print(f"Его позиция в массиве: {pos}")
    del a

if __name__== "__main__":
    func()

'''
16.2 MiB - Для запуска программы.
1.9 MiB - на создание списка а.
После удаления списка "a" освободилось 1.6 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
     6     16.2 MiB     16.2 MiB   @profile
     7                             def func():
     8     18.1 MiB      1.9 MiB       a = list(range(100000))
     9
    10     18.1 MiB      0.0 MiB       max_neg_elem = a[0]
    11     18.1 MiB      0.0 MiB       pos = 0
    12     18.1 MiB      0.0 MiB       for i in range(len(a)):
    13     18.1 MiB      0.0 MiB           if a[i] < 0:
    14                                         if max_neg_elem < a[i]:
    15                                             max_neg_elem = a[i]
    16                                             pos = i
    17
    18     18.1 MiB      0.0 MiB       print(f"Максимальный отрицательный элемент в массиве: {max_neg_elem}")
    19     18.1 MiB      0.0 MiB       print(f"Его позиция в массиве: {pos}")
    20     16.5 MiB      0.0 MiB       del a
'''