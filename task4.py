"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} составляет {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость автомобиля {self.name} составляет {self.speed} км/ч")
        if self.speed > 60:
            print("Превышена разрешенная скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость автомобиля {self.name} составляет {self.speed} км/ч")
        if self.speed > 40:
            print("Превышена разрешенная скорость!")


class PoliceCar(Car):
    pass


police = PoliceCar(80, "blue", "Mazda", True)
print(police.name, police.color, police.speed, police.is_police)
work = WorkCar(60, "green", "Volvo", False)
print(work.name, work.color, work.speed, work.is_police)
sport = SportCar(150, "red", "Ferrari", False)
print(sport.name, sport.color, sport.speed, sport.is_police)
town = TownCar(59, "blue", "Lada", False)
print(town.name, town.color, town.speed, town.is_police)

police.go()
work.stop()
sport.show_speed()
town.turn("налево")
work.show_speed()
town.show_speed()
