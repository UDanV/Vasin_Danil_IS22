"""
В квадратной матрице элементы на главной диагонали увеличить в 2 раза
"""
matrix = [[i+j for j in range(1, 4)] for i in range(3)]
print("Матрица до изменений:", matrix)
for i in range(len(matrix)):
    matrix[i][i] *= 2
print("Матрица после изменений:", matrix)
