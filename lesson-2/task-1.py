while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Введите операцию: ")
    if operation == "0":
        print("Прощай пользователь")
        break
    else:
        if operation == "/" and b == 0:
            print("На 0 делить нельзя")
        elif operation == "/":
            print(f"a / b = {a / b}")
        elif operation == "+":
            print(f"a + b = {a + b}")
        elif operation == "-":
            print(f"a - b = {a - b}")
        elif operation == "*":
            print(f"a * b = {a * b}")
        else:
            print("Ошибка: Такой операции нет")
