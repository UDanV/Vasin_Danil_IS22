def find_local_min():
    try:
        N = int(input("Введите размер списка: "))
        lst = []
        for i in range(N):
            lst.append(int(input("Введите элемент списка: ")))
        for i in range(1, N-1):
            if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
                print("Номер первого локального минимума: ", i)
                break
        else:
            print("Локальный минимум не найден")
    except ValueError:
        print("Ошибка: введено некорректное значение")

find_local_min()