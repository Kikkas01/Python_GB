"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        try:
            int(self.param)
        except ValueError:
            print("Некорректный формат числа")
            exit()

    @property
    def param_set(self):
        return self.param

    @param_set.setter
    def param_set(self, param):
        self.param = param


class Coat(Clothes):
    def consumption(self):
        super(Coat, self).consumption()
        return f"Расход ткани для пальто составляет {round((self.param / 6.5 + 0.5), 2)}"


class Costume(Clothes):
    def consumption(self):
        super(Costume, self).consumption()
        return f"Расход ткани для костюма составляет {round((self.param * 2 + 0.3), 2)}"


coat1 = Coat(42)
costume1 = Costume(165)
print(coat1.consumption())
print(costume1.consumption())
coat1.param = 56
print(coat1.param_set)
print(coat1.consumption())
print(f"Общий расход ткани составит {(coat1.param / 6.5 + 0.5) + (costume1.param * 2 + 0.3): .2f}")
coat2 = Coat("не число")
print(coat2.consumption())


