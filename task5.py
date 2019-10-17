from math import pow, sqrt, pi, asin

x1 = float(input('x1: '))
y1 = float(input('y1: '))

x2 = float(input('\nx2: '))
y2 = float(input('y2: '))

x3 = float(input('\nx3: '))
y3 = float(input('y3: '))

def lenSide(x1, y1, x2, y2):
  s1 = abs(x1 - x2)
  s2 = abs(y1 - y2)
  side = sqrt(pow(s1, 2) + pow(s2, 2))

  return side

side1 = lenSide(x1, y1, x2, y2)
side2 = lenSide(x2, y2, x3, y3)
side3 = lenSide(x3, y3, x1, y1)

print('\n1-я сторона', round(side1, 2))
print('2-я сторона', round(side2, 2))
print('3-я сторона', round(side3, 2))

print('\n')

perimetr = side1 + side2 + side3;

p = perimetr / 2;

square = sqrt(p*(p - side1)*(p - side2)*(p - side3))

print('Периметр: ', round(perimetr, 2))
print('Площадь: ', round(square, 2))

print('\n')

# 2 - e задание

def lenMedian(a, b, c):
  need = a
  median = 0.5*sqrt(2*b*b + 2*c*c - pow(need, 2))

  return median

m1 = lenMedian(side1, side2, side3)
m2 = lenMedian(side2, side1, side3)
m3 = lenMedian(side3, side1, side2)

print('\n1-я медиана', round(m1, 2))
print('2-я медиана', round(m2, 2))
print('3-я медиана', round(m3, 2))


def lenHeight(a):
  need = a
  height = (2*square) / need

  return height

h1 = lenHeight(side1)
h2 = lenHeight(side2)
h3 = lenHeight(side3)

print('\n1-я высота', round(h1, 2))
print('2-я высота', round(h2, 2))
print('3-я высота', round(h3, 2))


def lenBiss(a, b, c):
  need = a
  biss = (2 / (b+c)) * sqrt(b*c*p*(p - need))
  
  return biss

b1 = lenBiss(side1, side2, side3)
b2 = lenBiss(side2, side1, side3)
b3 = lenBiss(side3, side1, side2)

print('\n1-я биссектрисса', round(b1, 2))
print('2-я биссектрисса', round(b2, 2))
print('3-я биссектрисса', round(b3, 2))

# 3-е задание

def rInsde(a, b, c):
  r = sqrt(((p - a)*(p - b)*(p - c)) / p)

  return r

def rOutside(a, b, c):
  r = (a * b * c) / (4 * sqrt(p*(p - a)*(p - b)*(p - c)))

  return r

inRad = rInsde(side1, side2, side3)
outRad = rOutside(side1, side2, side3)

print('\nРадиус вписанной окрудности: ', round(inRad, 2))
print('Радиус описанной окружности: ', round(outRad, 2))

def findAngle(a):
  sinus = a / 2 * outRad
  alpha = (asin(sinus) / pi) * 180

  return alpha

angle1 = findAngle(side1)
angle2 = findAngle(side2)
angle3 = findAngle(side3)

print('\n1-й угол', round(angle1, 2))
print('2-й угол', round(angle2, 2))
print('3-й угол', round(angle3, 2))