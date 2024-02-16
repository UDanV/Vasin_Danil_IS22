"""
Составить генератор (yield), который выводит из строки только цифры.
"""
def digit_generator(string):
    for char in string:
        if char.isdigit():
            yield char

# Пример использования генератора
string = "Пример строки с цифрами 123 и символами 456"
digits = ''.join(digit_generator(string))
print("Цифры в строке:", digits)
