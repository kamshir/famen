# 3

from math import sqrt

s = float(input('Расстояние между машинами: '))

v1 = float(input('Скорость первой машины: '))
v2 = float(input('Сокрость второй машины: '))

a1 = float(input('Ускорение первой машины: '))
a2 = float(input('Ускорение второй машины: '))

# (a1 + a2) / 2 * t**2 + (v1+v2) * t - s = 0

a = (a1 + a2) / 2
b = v1 + v2

d = b**2 - 4 * a * s

if d < 0:
    print('Нет корней')

elif d == 0:
    x = -b/(2*a)
    print('Корень:', x)

else:
    x1 = (-b + sqrt(d)) // (2*a)
    x2 = (-b - sqrt(d)) // (2*a)
    print('x1:', x1)
    print('x2:', x2)

