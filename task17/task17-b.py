# 4

from math import cos, sin

a = float(input('Начало отрезка: '))
b = float(input('Конец отрезка: '))

k = 0

eps = float(input('Точность расчётов: '))

while True:
	c = (a + b) / 2
	fa = cos(a) + sin(a)
	fb = cos(b) + sin(b)
	fc = cos(c) + sin(c)
	if (fa * fc < 0):
		b = c
	else:
		a = c

	k += 1

	if (abs(b - a) > eps): 
		break

print('Корень уравнения:', c)

print('Кол-во делений:', k)