# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

try:
    num1 = int(input("Введите первое число\n"))
    num2 = int(input("Введите второе число\n"))
    num3 = int(input("Введите третье число\n"))

    if num1 < num2 and num1 < num3:
        if num2 < num3:
            print(f"{num2}")
        elif num2 > num3:
            print(f"{num3}")
    elif num2 < num1 and num2 < num3:
        if num1 < num3:
            print(f"{num1}")
        elif num1 > num3:
            print(f"{num3}")
    elif num3 < num1 and num3 < num2:
        if num1 < num2:
            print(f"{num1}")
        elif num1 > num2:
            print(f"{num2}")
    else:
        print(f"Невозможно найти среднее число")

except ValueError:
    print("Все значения должны быть целыми числами")
