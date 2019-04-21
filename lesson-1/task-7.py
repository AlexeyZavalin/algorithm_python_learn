print("Введите длины сторон предполагаемого треугольника:")
a = float(input("Первая сторона: "))
b = float(input("Вторая сторона: "))
c = float(input("Третья сторона: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a != b and a != c and b != c:
        print("Треугольник разносторонний")
    elif a == b and b == c:
        print("Треугольник равносторонний")
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print("Треугольник равнобедренный")
else:
    print("Треугольник не существует")
