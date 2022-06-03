# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

try:
    x1 = int(input("Введите x1\n"))
    y1 = int(input("Введите y1\n"))
    x2 = int(input("Введите x2\n"))
    y2 = int(input("Введите y2\n"))

    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2

    print(f"y = {k}x + {b}")

except ValueError:
    print("Все значения должны быть целыми числами")
except ZeroDivisionError:
    print("x1 не может быть равно x2")
