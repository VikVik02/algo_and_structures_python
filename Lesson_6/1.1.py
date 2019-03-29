# 4.	Определить, какое число в массиве встречается чаще всего.

from memory_profiler import profile

@profile
def func():
    a = list(range(100000))
    b = list(set(a))

    max_count = 0
    for i in range(len(b)):
        if max_count < a.count(b[i]):
            max_count = a.count(b[i])
            max_num = b[i]
    del a
    print(max_num)
    del b

if __name__== "__main__":
    func()

'''
Версия Python 3.7.2
64-разрядная ОС
16.2 MiB - Для запуска программы.
1.9 MiB - на создание списка а.
0.4 MiB - на создание множества b.
После удаления списка "a" и "b" освободилось 2.1 MiB.
Line #    Mem usage    Increment   Line Contents
================================================
     6     16.2 MiB     16.2 MiB   @profile
     7                             def func():
     8     18.1 MiB      1.9 MiB       a = list(range(100000))
     9     18.5 MiB      0.4 MiB       b = list(set(a))
    10
    11     18.5 MiB      0.0 MiB       max_count = 0
    12     18.5 MiB      0.0 MiB       for i in range(len(b)):
    13     18.5 MiB      0.0 MiB           if max_count < a.count(b[i]):
    14     18.5 MiB      0.0 MiB               max_count = a.count(b[i])
    15     18.5 MiB      0.0 MiB               max_num = b[i]
    16     18.0 MiB      0.0 MiB       del a
    17     18.0 MiB      0.0 MiB       print(max_num)
    18     16.4 MiB      0.0 MiB       del b
'''