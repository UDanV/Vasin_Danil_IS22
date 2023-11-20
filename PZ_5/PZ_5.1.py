def sum_user_numbers():
    start = int(input("Введите начало числового ряда: "))
    end = int(input("Введите конец числового ряда: "))
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


result = sum_user_numbers()
print(result)  # Выведет сумму числового ряда, введенного пользователем
