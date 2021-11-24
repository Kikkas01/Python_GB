"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод

"""

# Задание сделал с проверкой порядка режимов

from time import sleep


class TrafficLight:
    __colour = ["Red", "Yellow", "Green"]

    def running(self):
        if self.__colour[0] == "Red":
            print(f"{self.__colour[0]} color ON")
            sleep(7)
        else:
            print(f"Wrong color: {self.__colour[0]}. Running stopped")
            exit()
        if self.__colour[1] == "Yellow":
            print(f"{self.__colour[1]} color ON")
            sleep(2)
        else:
            print(f"Wrong color: {self.__colour[1]}. Running stopped")
            exit()
        if self.__colour[2] == "Green":
            print(f"{self.__colour[2]} color ON")
            sleep(4)
        else:
            print(f"Wrong color: {self.__colour[2]}. Running stopped")
            exit()


traffic_1 = TrafficLight()
traffic_1.running()


