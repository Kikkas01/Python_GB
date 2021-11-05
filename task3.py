# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    if min(var_1, var_2, var_3) == var_1:
        x = var_2
        y = var_3
    elif min(var_1, var_2, var_3) == var_2:
        x = var_1
        y = var_3
    else:
        x = var_1
        y = var_2
    return x + y


print(my_func(7, 4, 5))





