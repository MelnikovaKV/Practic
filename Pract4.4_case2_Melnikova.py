'''Задание №2
Создайте класс Autobus, который наследуется от класса Transport.
Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
Используйте переопределение метода.
Используйте следующий код для родительского класса транспортного
средства:
class Transport:
def __init__(self, name, max_speed, mileage):
self.name = name
self.max_speed = max_speed
self.mileage = mileage
def seating_capacity(self, capacity):
return f"Вместимость одного автобуса {self.name} {capacity}
пассажиров"
Ожидаемый результат вывода:
Вместимость одного автобуса Renault Logan: 50 пассажиров'''

class Transport(object):
    name = 'VOLVO'
    max_speed = 150
    mileage = 34000

    def __init__(self, n, ms, mil):
        self.name = n
        self.max_speed = ms
        self.mileage = mil

class Autobus(Transport):
    capacity = 50

    def __init__(self, n, ms, mil, capacity):
        super().__init__(n, ms, mil)
        self.capacity = capacity

    def seating_capacity(self):
        print(f"Вместимость одного автобуса {self.name} {self.capacity} пассажиров")
    

logan = Autobus('Renault Logan', 200, 35000, 50)
logan.seating_capacity()
