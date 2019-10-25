# 5
from math import sin, cos, radians

angle = float(input('Введите угол (в градусах): '))

angleRad = radians(angle)

print("Синус: {}".format(sin(angleRad)))
print("Косинус: {}".format(cos(angleRad)))