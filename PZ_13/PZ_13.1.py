"""
В квадратной матрице элементы на главной диагонали увеличить в 2 раза
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # пример квадратной матрицы
for i in range(len(matrix)):
    matrix[i][i] *= 2  # умножаем элементы на главной диагонали на 2
print(matrix)