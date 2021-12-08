"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой
"""


class ZeroDivision(Exception):

    def __init__(self, message="Попытка деления на ноль!"):
        self.message = message

    def __str__(self):
        return f"{self.message}"


inp = input("Введите делимое: ")
inp1 = input("Введите делитель: ")

try:
    inp1 = int(inp1)
    inp = int(inp)
    if int(inp1) == 0:
        raise ZeroDivision()
except ValueError:
    print("Некорректный формат числа!")
except ZeroDivision as err:
    print(err)
else:
    print(f"Результат деления равен {(int(inp) / int(inp1)):.2f}")

