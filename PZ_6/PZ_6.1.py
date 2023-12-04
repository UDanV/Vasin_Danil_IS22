# Дан первый член A и разность D арифметической прогрессии. Сформировать и
# вывести список размера 10, содержащий 10 первых членов данной прогрессии: A, A
# + D, A + 2*D, A + 3*D, ... .
def arithmetic_progression():
    try:
        # Вводим члены прогрессии
        A = int(input("Введите первый член прогрессии: "))
        D = int(input("Введите разность прогрессии: "))
        lst = []
        # Создаем цикл, который будет добавлять в список значения, умноженные на разность прогрессии
        for i in range(10):
            lst.append(A + i*D)
        print("Первые 10 членов прогрессии: ", lst)
    except ValueError:
        print("Ошибка: введено некорректное значение")

arithmetic_progression()