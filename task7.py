"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.

"""

with open("task7.txt", encoding='utf-8') as txt_file_7:
    quantity = int(len(txt_file_7.readlines()))
with open("task7.txt", encoding='utf-8') as txt_file_7:
    firms = {}
    avg_profit = {}
    avg_calc = []
    for line in txt_file_7:
        title = line.split()[0]
        profit = int(line.split()[2]) - int(line.split()[3])
        firms[title] = profit
        if profit < 0:
            quantity -= 1
        else:
            avg_calc.append(profit)
    avg_profit["average_profit"] = sum(avg_calc)/quantity
    info = [firms, avg_profit]
    print(info)

import json
with open("task7.json", "w") as json_file_7:
    json.dump(info, json_file_7)


