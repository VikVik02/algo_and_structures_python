"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

quant = int(input('Количество предприятий'))
company = collections.defaultdict(list)

for i in range(quant):
    name = input(f'Введите имя {i + 1}-й компании: ')
    profit = [(int(input(f'Введите прибыль за {j+1}-й квартал: '))) for j in range(4)]
    company[name] = sum(profit)

average_profit = sum(company.values()) / quant
print(f'Средняя прибыль {average_profit}')

for i in company:
    if company[i] < average_profit:
        print(f'Предприятие "{i}" имеет прибыль ниже средней: ({company[i]})')
    elif company[i] > average_profit:
        print(f'Предприятие "{i}" имеет прибыль выше средней: ({company[i]})')
