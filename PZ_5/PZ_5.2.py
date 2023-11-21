# Импортируем библиотеку
import math
# Создаем функцию TrianglePS
def TrianglePS(a):
    try:
        perimeter = 3 * a
        area = (a ** 2) * math.sqrt(3) / 4
        return perimeter, area
    except ValueError:
        print("Ошибка: Введите корректное числовое значение.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Создаем цикл, который 3 раза будет запрашивать у пользователя сторону треугольника
for i in range(3):
    try:
        side = float(input("Введите сторону треугольника: "))
        perimeter, area = TrianglePS(side)
        print(f"Периметр треугольника со стороной {side} равен {perimeter}, а площадь равна {round(area, 2)}")
    except ValueError:
        print("Ошибка: Введите корректное числовое значение.")
    except Exception as error:
        print(f"Произошла ошибка: {error}")
