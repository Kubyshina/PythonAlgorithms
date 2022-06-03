# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

try:
    year = int(input("Введите год"))

    if year % 4 != 0:
        print(f"Год не високосный")
    elif year % 400 == 0:
        print(f"Год не високосный")
    else:
        print(f"Год високосный")

except ValueError:
    print("Значение должно быть целым числом")