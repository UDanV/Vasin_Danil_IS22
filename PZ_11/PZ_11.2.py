"""
Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно заменив символы третей
строки их числовыми кодами
"""

import string

with open('text18-3.txt', 'r', encoding="utf-16") as file:
    content = file.readlines()
    for i in range(4):
        punctuation = sum([1 for char in content[i] if char in string.punctuation])
        print(f"Строка {i + 1}: {content[i].strip()} (количество знаков пунктуации: {punctuation})")

with open('data.txt', 'w') as file:
    for i, line in enumerate(content):
        if i == 2:
            encodeLine = ''.join([str(ord(char)) for char in line])
            file.write(encodeLine + '\n')
        else:
            file.write(line)