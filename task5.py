"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_of_numbers():
    try:
        start_input = input("Введите строку чисел, разделённых пробелами ").split()
        start_line = [float(i) for i in start_input]
        start_result = sum(start_line)
        result = 0
        print(start_result)
        z = 0
        while z == 0:
            continue_input = input(
                "Введите строку чисел, разделённых пробелами, "
                "если требуется завершить работу - введите в конце спецсимвол: '/' ").split()
            if continue_input[-1] == "/":
                cont_line = [float(i) for i in continue_input[0:-1]]
                z = 1
                result = sum(cont_line) + start_result
            else:
                cont_line = [float(i) for i in continue_input]
                result = sum(cont_line) + start_result
                start_result = result
                print(result)
        return print(result)
    except ValueError:
        print("Ошибка ввода данных")


sum_of_numbers()


