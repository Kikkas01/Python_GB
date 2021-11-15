# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open("task5.txt", "w", encoding='utf-8') as txt_file_5:
        start_input = input("Введите строку чисел, разделённых пробелами: ")
        try:
            start_line = [float(i) for i in start_input.split()]
        except ValueError:
            print("Необходимо ввести числа!")
        txt_file_5.writelines(start_input)
    print(sum(start_line))

except IOError:
    print("error")

