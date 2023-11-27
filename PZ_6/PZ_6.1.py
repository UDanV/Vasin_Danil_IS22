def arithmetic_progression():
    try:
        A = int(input("Введите первый член прогрессии: "))
        D = int(input("Введите разность прогрессии: "))
        lst = []
        for i in range(10):
            lst.append(A + i*D)
        print("Первые 10 членов прогрессии: ", lst)
    except ValueError:
        print("Ошибка: введено некорректное значение")

arithmetic_progression()