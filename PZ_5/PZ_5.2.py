import math

def TrianglePS(a):
    perimeter = 3 * a
    area = (a ** 2) * math.sqrt(3) / 4
    return perimeter, area

for i in range(3):
    side = float(input("Введите сторону треугольника: "))
    perimeter, area = TrianglePS(side)
    print(f"Периметр треугольника со стороной {side} равен {perimeter}, а площадь равна {area}")
