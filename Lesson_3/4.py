# 4.	Определить, какое число в массиве встречается чаще всего.

#list.count(x) - возвращает количество элементов со значением x

a = [1, -2, 5, 5, 6, 3, 3, 3, 7, 3, -2, -8, 9, -2]
b = list(set(a))
print()

max_count = 0
for i in range(len(b)):
    if max_count < a.count(b[i]):
        max_count = a.count(b[i])
        max_num = b[i]
    print(f"Количество элементов в массиве со значением {b[i]}: ", a.count(b[i]))
print(f"В массиве чаще всего встречается число {max_num}")
