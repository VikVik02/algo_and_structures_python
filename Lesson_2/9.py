"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

quant = int(input("Введите количество чисел"))

max_num = 0
max_sum = 0

while quant != 0:
    num = int(input("Введите число"))
    while num != 0:
        summ = 0
        maxx = num
        while num > 0:
            summ += num % 10
            num //= 10
        if summ > max_sum:
            max_sum = summ
            max_num = maxx
    quant -= 1

print(f"Число {max_num} имеет максимальную сумму {max_sum}")


