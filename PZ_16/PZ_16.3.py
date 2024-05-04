import pickle

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

def save_def(counters, filename):
    with open(filename, 'wb') as f:
        pickle.dump(counters, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

counter1 = Counter(5)
counter2 = Counter(10)
counter3 = Counter(15)

counters = [counter1, counter2, counter3]
save_def(counters, 'counters.bin')

loaded_counters = load_def('counters.bin')

for counter in loaded_counters:
    print(f"Стартовое значение: {counter.value}, Инкремент: {counter.increment()}, Декремент: {counter.decrement()}")
