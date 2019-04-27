x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

if y1 - y2 == 0 and x2 - x1 == 0:
    print("Нет уравнения")
else:
    c = x1 * y2 - x2 * y1
    if c < 0:
        print(f"Уравнение для ваших координат: {(x1 - y2)}*x + {x2 - x1}*y {c} = 0")
    elif c > 0:
        print(f"Уравнение для ваших координат: {(x1 - y2)}*x + {x2 - x1}*y + {c} = 0")
    else:
        print(f"Уравнение для ваших координат: {(x1 - y2)}*x + {x2 - x1}*y = 0")
