from math import sqrt

a = float(input('Первое число: '))
b = float(input('Второе число: '))
c = float(input('Третье число: '))

d = b ** 2 - 4 * a * c

if d > 0:
    print('Уравнение имеет два корня')
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
elif d == 0:
    print('Уравнение имеет один корень')
    x1 = -b / (2 * a)
    print(x1)
else:
    print('Уравнение не имеет корней')
