# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

lol = [[5, 5, 12, 4, 9],
       [1, 7, 10, 8, 16],
       [5, 17, 3, 0, 3],
       [3, 8, 15, 19, 2],
       [9, 6, 5, 18, 6]]

kek = []

lol = list(zip(*lol))

for i in lol:
    mn = min(i)
    kek.append(mn)

print(f"Минимальные элементы каждого столбца матрицы: {kek}")

mx = max(kek)
print(f"Максимальный элемент среди минимальных элементов {mx}")
