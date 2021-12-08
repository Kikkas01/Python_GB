"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:

    def __init__(self, date: str):
        self.date = date

    @classmethod  # второй вариант решения закомментирован
    def transform(cls, data):
        # result = []
        try:
            return [int(data.split("-")[0]), int(data.split("-")[1]), int(data.split("-")[2])]
            # for el in data.split("-"):
            #     result.append(el)
            # return f"день: {int(result[0])}, месяц: {int(result[1])}, год: {int(result[2])}"
        except IndexError:
            print("Задайте дату в правильном формате ДД-ММ-ГГГГ")

    @staticmethod
    def validate(data):
        if int(data.split("-")[0]) > 12:
            return "Месяца с таким номером не существует"
        elif int(data.split("-")[1]) > 31 and int(data.split("-")[0]) in [1, 3, 5, 7, 8, 10, 12]:
            return "Задано несуществующее количество дней в месяце"
        elif int(data.split("-")[1]) > 30 and int(data.split("-")[0]) in [4, 6, 9, 11]:
            return "Задано несуществующее количество дней в месяце"
        elif int(data.split("-")[1]) > 29 and int(data.split("-")[0]) == 2:
            return "Задано несуществующее количество дней в месяце"
        elif len((data.split("-")[2])) < 4:
            return "Год задан в неверном формате"
        else:
            return "Дата корректна"


print(Data.transform("12-12-2025"))
print(Data.transform("12122025"))
print(Data.validate("12-12-2025"))
print(Data.validate("12-32-2025"))
print(Data.validate("40-12-2025"))
print(Data.validate("12-12-225"))




