import math
choose = 0
while choose != 11:
    print('1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Возведение в степень\n6 - Квадратный корень\n7 - Факториал\n8 - Синус\n9 - Косинус\n10 - Тангенс\n11 - Выйти')
    choose = int(input('Операция: '))
    if choose == 1:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        print('Ответ: ', a+b)
    if choose == 2:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        print('Ответ: ', a-b)
    if choose == 3:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        print('Ответ: ', a*b)
    if choose == 4:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        if b != 0:
            print('Ответ: ', a/b)
        else:
            print('На ноль делить нельзя')
    if choose == 5:
        a = float(input('Введите число: '))
        b = float(input('Введите степень: '))
        print('Ответ: ', a**b)
    if choose == 6:
        a = float(input('Введите число: '))
        if a >= 0:
            print('Ответ: ', math.sqrt(a))
        else:
            print('Нужно ввести число не меньше 0')
    if choose == 7:
        a = float(input('Введите число: '))
        if a >= 0:
            print('Ответ: ', math.factorial(int(a)))
        else:
            print('Нужно ввести число не меньше 0')
    if choose == 8:
        a = float(input('Введите число: '))
        print('Ответ: ', math.sin(a))
    if choose == 9:
        a = float(input('Введите число: '))
        print('Ответ: ', math.cos(a))
    if choose == 10:
        a = float(input('Введите число: '))
        print('Ответ: ', math.tan(a))

