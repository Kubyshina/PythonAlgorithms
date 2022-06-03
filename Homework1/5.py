# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

try:
    number = int(input("Введите номер буквы (от 1 до 26)\n"))
    if 0 < number < 27:
        letter = chr(ord('a') + number - 1)
        print(letter)
    else:
        print("Неверный ввод")

except ValueError:
    print("Значение должно быть целым числом")
