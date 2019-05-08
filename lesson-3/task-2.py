import random

array = [random.randint(1, 50) for _ in range(10)]
print(array)
even = []

for i, item in enumerate(array):
    if item % 2 == 0:
        even.append(i)

print(even)
