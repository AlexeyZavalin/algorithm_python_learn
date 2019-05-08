import sys

sys.setrecursionlimit(3000)


def calc_sum(n, number, changer, operation, sum_row):
    if n == 1:
        return sum_row + number
    if operation == "-":
        return calc_sum(n - 1, number - changer, changer / 2, '+', sum_row + number)
    if operation == "+":
        return calc_sum(n - 1, number + changer, changer / 2, '-', sum_row + number)


n = int(input("Введите размер ряда: "))
result = calc_sum(n, 1, 1.5, "-", 0)
print(f"Сумма элементов = {result}")
