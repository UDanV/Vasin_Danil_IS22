import random

def generate_sequences(N):
    # Генерируем исходную последовательность из N случайных чисел
    original_sequence = [random.randint(0, 100) for _ in range(N)]

    # Разделяем на две последовательности
    multiple_of_three = [num for num in original_sequence if num % 3 == 0]
    other_numbers = [num for num in original_sequence if num % 3 != 0]

    return original_sequence, multiple_of_three, other_numbers

# Пример использования функции
N = random.randint(5, 15)
original_sequence, multiple_of_three, other_numbers = generate_sequences(N)
print("Исходная последовательность:", original_sequence)
print("Числа, кратные трем:", multiple_of_three)
print("Остальные числа:", other_numbers)
print("Количество элементов, кратных трем:", len(multiple_of_three))
print("Количество остальных элементов:", len(other_numbers))
