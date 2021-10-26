# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# Решение: сначала находим последнюю цифру в числе и оставляем от числа часть без неё
# далее запускаем цикл сравнения полученного значения и перезаписываем его новым, если оно больше,
# снова обрезая число n на единицу.
n = int(input("Введите целое положительное число:"))
if n < 1:
    print("Число не является целым положительным")
else:
    digit = n % 10
    n = n // 10
    while n > 0:
        if n % 10 > digit:
            digit = n % 10
        n = n // 10
print(digit)


