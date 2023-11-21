# Создаем функцию sum_user_numbers
def sum_user_numbers():
    try:
        start = int(input("Введите начало числового ряда: "))
        end = int(input("Введите конец числового ряда: "))
        total = 0
        # Создаем цикл, который будет выводить ответ в зависимости от введенных данных
        for i in range(start, end + 1):
            total += i
        return total
    except ValueError:
        print("Ошибка: Введите корректное числовое значение.")
    except Exception as error:
        print(f"Произошла ошибка: {error}")

result = sum_user_numbers()
print(result) # Выведет сумму числового ряда, введенного пользователем
