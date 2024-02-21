"""
Из матрицы сформировать массив из положительных четных элементов, найти их
сумму и среднее арифметическое.
"""
matrix = [[i+j for j in range(-1, 4)] for i in range(4)]
print("Исходная матрица", matrix)
positive_even = []  # Здесь будем хранить положительные четные элементы
for row in matrix:
    for element in row:
        if element > 0 and element % 2 == 0:  # Проверка на четность и положительность
            positive_even.append(element)  # Аппендим (добавляем) элемент в массив
print("Массив положительных четных элементов:", positive_even)
print("Сумма положительных четных элементов:", sum(positive_even))
print("Среднее арифметическое положительных четных элементов:", round(sum(positive_even) / len(positive_even), 1))
