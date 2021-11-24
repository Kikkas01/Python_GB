"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:

    def __init__(self, name, surname, position, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


new_pos = Position("Sergey", "Ivanov", "CEO", 32500.5, 6200.85)

print(f"Проверка атрибутов: name - {new_pos.name}, surname - {new_pos.surname}, position - {new_pos.position},"
      f"_income - {new_pos._income}")
print(f"Сотрудник {new_pos.get_full_name()} получил {new_pos.get_total_income()} рублей дохода")

