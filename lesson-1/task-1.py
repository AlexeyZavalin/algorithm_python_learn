a = int(input("Введите трехзначное число: "))
first = a // 100
second = a // 10 % 10
third = a % 10
print(f"сумма цифр числа a = {first + second + third}")
