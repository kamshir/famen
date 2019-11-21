# 3

from math import cos, sin, pi

a = float(input('Начало отрезка: '))
b = float(input('Конец отрезка: '))

eps = float(input('Точность расчётов: '))

def f(x):
	return sin((pi * x) / 180) - 1 / x

def find(x0, x1, eps):
	while True:
		x = (x0 + x1) / 2
		func = f(x)

		if (func > 0):
			x0 = x
		else:
			x1 = x

		if (abs(x1 - x0) > eps): 
			break

		return c

c = find(a, b, eps)

print('Корень уравнения:', c)