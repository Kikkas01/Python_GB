# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("task3.txt", encoding='utf-8') as txt_file_3:
    print("Указанные ниже сотрудники получают менее 20000:")
    for line in txt_file_3:
        if float(line.split()[-1]) < 20000.00:
            print(line.split()[0])
        else:
            continue
with open("task3.txt", encoding='utf-8') as txt_file_3:
    salary = []
    for line in txt_file_3:
        salary.append(float(line.split()[-1]))
    print(f"Средняя зарплата сотрудников составила {sum(salary) / len(salary)}")

print(txt_file_3.closed)
