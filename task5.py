"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.

"""


class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой с наименованием {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом с наименованием {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером с наименованием {self.title}")


x = Stationery("Any")
y = Pen("Bic")
z = Pencil("Faber Castell")
a = Handle("Inkwell")
x.draw()
y.draw()
z.draw()
a.draw()

