"""
Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
инкремента и декремента значения
"""
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

counter = Counter()
print("Стартовое значение:", counter.value)
counter.increment()
print("Инкремент:", counter.value)
counter.decrement()
counter.decrement()
print("Декремент:", counter.value)
