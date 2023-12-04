# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
# символа строки, нарушающего алфавитный порядок.
def first_unordered_letter_index(s):
    try:
        # Игнорируем не-буквенные символы
        letters = [char for char in s if char.isalpha()]

        for i in range(1, len(letters)):
            if letters[i] < letters[i - 1]:
                return i
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return -1

# Получение строки от пользователя
user_input = input("Введите строку с цифрами и латинскими буквами: ")
result = first_unordered_letter_index(user_input)

print(f"Результат: {result}")
