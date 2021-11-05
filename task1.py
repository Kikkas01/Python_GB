# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Вариант решения 1
def split(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
print(split(first, second))


# Вариант решения 2
def split():
    try:
        first = float(input("Введите первое число: "))
        second = float(input("Введите второе число: "))
        result = first / second
    except ValueError:
        return
    except ZeroDivisionError:
        return
    return result


print(split())




