# Определение размера скидки в зависимости от потраченной суммы

try:
    # Вводим сумму покупки
    purchase_amount = float(input("Введите сумму покупки: "))

    # Проверяем размер скидки, исходя из потраченной суммы
    if purchase_amount < 0:
        raise ValueError("Сумма покупки не может быть отрицательной")
    elif purchase_amount < 500:
        discount = 2
    elif purchase_amount < 1000:
        discount = 3
    elif purchase_amount < 1500:
        discount = 4
    elif purchase_amount < 2000:
        discount = 5
    else:
        discount = 0.0

    # Выводим результат
    if discount == 5:  # Если размер скидки составляет 5 процентов, выводим слово с правильным склонением
        print("Размер скидки составляет:", discount, "процентов")
    else:
        print("Размер скидки составляет:", discount, "процента")

except ValueError as error:
    print("Ошибка:", error)
