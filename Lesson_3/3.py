#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

N = 10
a = [0] * N
for i in range(N):
    a[i] = random.randint(1, 100)
    print(a[i], end = ' ')
print()

max_a = a[0]
min_a = a[0]

max_index = 0
for i in range(len(a)):
    if max_a < a[i]:
        max_a = a[i]
        max_index = i
print("Максимальный элемент: ", max_a)

min_index = 0
for i in range(len(a)):
    if min_a > a[i]:
        min_a = a[i]
        min_index = i
print("Минимальный элемент: ", min_a)

a[min_index], a[max_index] = a[max_index], a[min_index]
print(a)