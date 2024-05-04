"""
Создайте класс "Автомобиль", который содержит информацию о марке, модели и
годе выпуска. Создайте класс "Грузовик", который наследуется от класса
"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
информацию о количестве пассажиров
"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})" # Выводим в виде строки

class Truck(Car):
    def __init__(self, brand, model, year, payload):
        super().__init__(brand, model, year)
        self.payload = payload

    def __str__(self):
        return f"{super().__str__()} - Грузоподъемность: {self.payload} тонн" # Выводим в виде строки

class PassengerCar(Car):
    def __init__(self, brand, model, year, num_passengers):
        super().__init__(brand, model, year)
        self.num_passengers = num_passengers

    def __str__(self):
        return f"{super().__str__()} - Вместимость: {self.num_passengers} человек" # Выводим в виде строки

myCar = PassengerCar("Toyota", "Camry 40", 2018, 5)
myTruck = Truck("Mercedes", "Actross", 2020, 20)

print(myCar)
print(myTruck)