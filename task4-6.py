"""
Задание4:
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Задание 5:
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

Задание 6:
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipment:

    def __init__(self, model: str, serial_number: str, price: float, tech_type: str = "OfficeEquipment"):
        self.model = model
        self.serial_number = serial_number
        self.price = price
        self.tech_type = tech_type
        self.el = {"Модель": model, "Цена": price, "Тип": self.tech_type}


class Printer(OfficeEquipment):
    def __init__(self, model, serial_number, price, laser: bool, tech_type="printers"):
        super(Printer, self).__init__(model, serial_number, price, tech_type)
        self.laser = laser


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_number, price, resolution: str, tech_type="scanners"):
        super(Scanner, self).__init__(model, serial_number, price, tech_type)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, model, serial_number, price, performance: int, tech_type="xeroxes"):
        super(Xerox, self).__init__(model, serial_number, price, tech_type)
        self.performance = performance


class OfficeEquipmentStorage:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.products = []

    def entry(self, products: dict):
        if len(self.products + self.products) > self.capacity:
            print("На складе закончилось свободное место")
            exit()
        else:
            self.products.append(products)

    def disposal(self, products: dict):
        self.products.remove(products)


pr = Printer("Canon", "123k13", 1265.2, True)
xer1 = Xerox("Xerox", "8743gd3", 2569.5, 256)
xer2 = Xerox("XXX", "12315rer", 3600, 525)
sc1 = Scanner("YYY", "92834982", 3651.22, "1280х1230")
print(pr.el)
st1 = OfficeEquipmentStorage(4)
st1.entry(pr.el)
st1.entry(xer1.el)
st1.entry(xer2.el)
print(st1.products)
st1.disposal(pr.el)
print(st1.products)
st1.entry(sc1.el)
st1.entry(pr.el)
print(st1.products)

