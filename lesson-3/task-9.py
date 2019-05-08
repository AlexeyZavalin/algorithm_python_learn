import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
mins = matrix[0]

for line in matrix:
    print(line)
    for i, item in enumerate(line):
        if line[i] < mins[i]:
            mins[i] = item

print(mins)

max_ = mins[0]

for item in mins:
    if item > max_:
        max_ = item

print(f'Максимальный элемент среди минимальных по столбцам: {max_}')
