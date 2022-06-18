#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. 

import random

array = [random.randint(1, 100) for i in range(10)]
print(array)

max = array[0]
max_i = 0
min = array[0]
min_i = 0

for i in range(len(array)):
    if array[i] > max:
        max = array[i]
        max_i = i
    if array[i] < min:
        min = array[i]
        min_i = i

array[max_i] = min
array[min_i] = max

print(array)

#[5, 7, 66, 42, 18, 31, 46, 69, 83, 71]
#[83, 7, 66, 42, 18, 31, 46, 69, 5, 71]