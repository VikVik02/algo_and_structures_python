"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

a = [-3, 5, 8, 30, 3, 6, 11, -1, -4, 23, 5]

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




