"""
Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
86532547891), а во второй с некорректными номерами телефонов. Посчитать
полученные строки в каждом файле.
"""
# Импортируем библиотеку
import re

# Открываем файл
with open('hotline.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

correct_file = open('correct_phones.txt', 'w', encoding="utf-8")
incorrect_file = open('incorrect_phones.txt', 'w', encoding="utf-8")

# Создаем параметр, по которому будут находится номера телефонов
phone_pattern = re.compile(r'\b\d{11}\b')

# Счётчики
correct_count = 0
incorrect_count = 0

# Проходимся циклом по каждой линии, если нашли совпадение, добавляем единицу и записываем строку в файл
for line in lines:
    phone_numbers = re.findall(phone_pattern, line)
    if phone_numbers:
        correct_file.write(line)
        correct_count += 1
    else:
        incorrect_file.write(line)
        incorrect_count += 1

# Закрываем файлы
correct_file.close()
incorrect_file.close()

print(f'Количество корректных номеров телефонов: {correct_count}')
print(f'Количество некорректных номеров телефонов: {incorrect_count}')