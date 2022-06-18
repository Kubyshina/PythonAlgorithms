# 4. Определить, какое число в массиве встречается чаще всего. 

from collections import OrderedDict
import random


array = [random.randint(1, 10) for i in range(20)]
print(array)

unique = set(array)
counter = {}
for i in unique:
    counter[i] = 0

for i in array:
    counter[i] +=1

max = 0
max_num = 0
for i in counter.keys():
    if counter[i] > max:
        max = counter[i]
        max_num = i

print(f"Чаще всего встречается число {max_num} - {counter[max_num]} раз.")

#[4, 6, 3, 9, 7, 3, 4, 4, 4, 9, 7, 10, 3, 6, 4, 3, 10, 3, 2, 4]
#Чаще всего встречается число 4 - 6 раз.