import random

array = [random.randint(-50, 50) for _ in range(10)]
print(array)
index = -1

for i, item in enumerate(array):
    if item < 0 and index == -1:
        index = i
    elif item < 0 and item > array[index]:
        index = i

print(f'Индекс: {index}, значение: {array[index]}')
