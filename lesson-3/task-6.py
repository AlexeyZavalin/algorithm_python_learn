import random

array = [random.randint(1, 50) for _ in range(10)]
print(array)
sum_ = 0
min_index, max_index = 0, 0

for i, item in enumerate(array):
    if item > array[max_index]:
        max_index = i
    if item < array[min_index]:
        min_index = i

print(min_index, max_index)

for item in array[min_index + 1: max_index]:
    sum_ += item

print(f'Сумма между максимальным и минмальным элементами: {sum_}')
