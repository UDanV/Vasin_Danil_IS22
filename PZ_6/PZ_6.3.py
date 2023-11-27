def swap_pairs():
    try:
        N = int(input("Введите размер списка (четное число): "))
        if N % 2:
            raise ValueError("Размер списка должен быть четным")
        if N < 0:
            raise ValueError("Размер списка не может быть отрицательным числом")
        lst = []
        for i in range(N):
            lst.append(int(input("Введите элемент списка: ")))
        for i in range(0, N-1, 2):
            lst[i], lst[i+1] = lst[i+1], lst[i]
        print("Измененный список:", lst)
    except ValueError as error:
        print("Ошибка:", error)

swap_pairs()