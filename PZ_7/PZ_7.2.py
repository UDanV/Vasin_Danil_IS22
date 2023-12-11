# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
# символа строки, нарушающего алфавитный порядок.
def check_alphabetic_order(s):
    try:
        if not s:
            return -1
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                return i + 1
        return 0
    except Exception as error:
        print(f"Ошибка: {error}")

input_str = input("Введите строку: ")  # Ввод пользователем строки
result = check_alphabetic_order(input_str)
if result == -1:
    print("Ошибка. Строка пуста")
elif result != 0:
    print(f"Номер первого символа, нарушающего алфавитный порядок: {result + 1}")
else:
    print("Строка упорядочена по алфавиту")