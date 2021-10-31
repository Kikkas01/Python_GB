# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# Решение через list:
month = input("Введите номер месяца в виде целого числа:")
if not month.isdigit():
    print("Неверный формат числа")
    exit()
month = int(month)

spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]

if month in spring:
    print("Весна")
elif month in summer:
    print("Лето")
elif month in autumn:
    print("Осень")
else:
    print("Зима")

# Решение через dict:
month = input("Введите номер месяца в виде целого числа:")
if not month.isdigit():
    print("Неверный формат числа")
    exit()
month = int(month)

month_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна",
              5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
              9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
for key, value in month_dict.items():
    if month == key:
        print(value)