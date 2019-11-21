#3

from math import sin, cos, pi

x0 = float(input('x0: '))

y0 = float(input('y0: '))

v0 = float(input('v0: '))

angle = float(input('angle: '))

radius = float(input('radius: '))

x = float(input('X: '))

y = float(input('Y: '))

g = 9.81

print('Time\t\t', 'X\t\t', 'Y')

t = 0

aInRad = (angle * 180) / pi

vx0 = v0 * cos(aInRad)

t = round((x - x0) / vx0, 2)

vy0 = v0 * sin(aInRad)

x1 = round(x0 + vx0 * t, 2)

y1 = round(y0 + vy0 * t - (g*t**2) / 2, 2)

# 4

h = vy0 * t - (g*t**2) // 2

print('Макс. Высота:', h)

# 5

