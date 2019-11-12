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

else:
    x1 = (-b + sqrt(d)) // (2*a)
    x2 = (-b - sqrt(d)) // (2*a)
    if x1 < 0:
	x = x2
    else:
	x = x1

t = x

print('Время:', t)

#4

# s = u0t - (a*t**2)/2

s1 = v1*t - (a1 * t**2) // 2
s2 = v2*t - (a2 * t**2) // 2

print('Расстояние первой машины:', s1)
print('Расстояние второй машины:', s2)


#5

fuel = float(input('Стоимость бензина: '))

c1 = s1 / 100
sl1 = c1 * fuel

c2 = s2 / 100
sl2 = c2 * fuel

print('Сумма первого авто:', sl1)
print('Сумма второго авто:', sl2)


