"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

def recursion(num):
    if num > 0:
        s = str(num % 10)
        s += str(recursion(num // 10))
        return s
    elif num == 0:
        return ''


num = int(input("Введите число"))
print(recursion(num))