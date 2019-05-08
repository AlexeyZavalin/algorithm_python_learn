import sys

sys.setrecursionlimit(3000)


def return_inverse(a):
    if a < 10:
        return int(a)
    b = int(a % 10)
    a = (a - b) / 10
    return f"{b}{return_inverse(a)}"


number = int(input("Введите число: "))
result = '' + return_inverse(number)
print(f"{number} inverse {result}")
