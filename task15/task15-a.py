#3

from math import sin, cos, pi

x0 = float(input('Нач. Коорд. X: '))

y0 = float(input('Нач. Коорд. Y: '))

v0 = float(input('Нач. Скорость снаряда: '))

angle = float(input('Угол ствола пушки: '))

radius = float(input('Радиус поражения: '))

x = float(input('X: '))

y = float(input('Y: '))

g = 9.81

print('Время T\t\t', 'X\t\t', 'Y')

aInRad = (angle * 180) // pi

vx0 = v0 * cos(aInRad)

print('\t\t', x0, '\t\t' ,y0)
