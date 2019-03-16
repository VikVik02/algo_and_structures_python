# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = []
for i in range(2, 100):
    a.append(i)
print(a)

s = 0
for j in range(2, 10):
    for i in range(len(a)):
        if a[i] % j == 0:
            s += 1
print(s)

