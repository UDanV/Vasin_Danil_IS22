"""
Средствами языка Python сформировать текстовый файл (.txt) содержащий
последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида,
предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:
"""

# Запишем в файл data_1.txt структуру данных - список
l = ['-99 6 12 -36 20 45 100 -15']
frstFile = open('data_1.txt', 'w')
frstFile.writelines(l)
frstFile.close()

# Дублируем список в новый файл data_4.txt
scndFile = open('data_2.txt', 'w')
scndFile.write('Исходные данные: ')
scndFile.writelines(l)
scndFile.close()

# разбиваем строку и ее значения преобразуем в числа
frstFile = open('data_1.txt')
k = frstFile.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
frstFile.close()

# Ищем минимальный элемент в файле data_1.txt и записываем в файл data_2.txt
frstFile = open('data_1.txt')
min = min(k)
frstFile.close()

# Ищем четные элементы и возводим их в квадрат
frstFile = open("data_1.txt")
event = [x**2 for x in k if x % 2 == 0]

scndFile = open('data_2.txt', 'a') # открываем файл для дозаписи
scndFile.write('\n')
print('Количество элементов: ', len(k), file=scndFile)
print('Минимальный элемент: ', min, file=scndFile)
print('Квадраты четных элементов : ', event, file=scndFile)
print('Сумма квадратов четных элементов : ', sum(event), file=scndFile)
print('Среднее арифметическое суммы квадратов четных элементов : ', sum(event) / len(event), file=scndFile)
scndFile.close()