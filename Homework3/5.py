#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

import random

array = [random.randint(-10, 10) for i in range(10)]
print(array)

max_negative = -10
max_negative_i = 0
for i in range(len(array)):
    if max_negative < array[i] < 0 :
        max_negative = array[i]
        max_negative_i = i

print(f"Максимальный отрицательный элемент массива {max_negative}, его позиция {max_negative_i}")

# [-6, 1, 0, 1, 10, -2, 8, -1, 6, -7]
# Максимальный отрицательный элемент массива -1, его позиция 7