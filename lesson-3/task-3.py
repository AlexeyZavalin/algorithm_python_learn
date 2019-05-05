import random

array = [random.randint(1, 50) for _ in range(10)]
print(array)
min_index, max_index = 0, 0
min_, max_ = array[min_index], array[max_index]

for i, item in enumerate(array):
    if item < min_:
        min_ = item
        min_index = i
    if item > max_:
        max_ = item
        max_index = i

array[min_index] = max_
array[max_index] = min_
print(array)
