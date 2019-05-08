odd = 0
even = 0
number = int(input("Введите число: "))

if number < 10:
    if number % 2 == 0:
        even = 1
    else:
        odd = 1
    print(f"Четных {even} | Нечетных {odd}")
else:
    while True:
        if number < 10:
            if number % 2 == 0:
                even += 1
            else:
                odd += 1
            break
        checking = number % 10
        if checking % 2 == 0:
            even += 1
        else:
            odd += 1
        number = (number - checking) / 10

    print(f"Четных {even} | Нечетных {odd}")
