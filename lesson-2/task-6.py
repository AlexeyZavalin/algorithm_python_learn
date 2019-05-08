from random import randint

a = randint(0, 100)

for i in range(10):
    answer = int(input("Введите ответ: "))
    if answer != a and answer > a:
        print('Ваше число больше')
    elif answer != a and answer < a:
        print('Ваше число меньше')
    else:
        print('Вы угадали')
        break

print(f'Правильный ответ {a}')
