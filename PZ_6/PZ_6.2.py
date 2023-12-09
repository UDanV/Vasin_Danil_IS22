# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).
import random
def find_local_min():
    try:
        N = int(input("Введите размер списка: "))
        if N == 0:
            print("Ваш список пуст")
            return
        lst = []
        for i in range(N):
            lst.append(random.randint(0, 10))
        print("Измененный список:", lst)

        # Проверка первого элемента
        if N == 1 or lst[0] < lst[1]:
            print("Номер первого локального минимума: 0")
            return

        # Проверка последнего элемента
        if lst[N - 1] < lst[N - 2]:
            print(f"Номер первого локального минимума: {N - 1}")
            return

        # Проверка элементов в середине списка
        for i in range(1, N - 1):
            if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
                print(f"Номер первого локального минимума: {i}")
                return
        print("Локальный минимум не найден")

    except ValueError:
        print("Ошибка: введено некорректное значение")


find_local_min()
