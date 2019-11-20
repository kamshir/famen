# 3

from math import sin, cos

def f(x):
  return sin(x) + cos(x)

k = 0
a = float(input('Начало: '))
b = float(input('Конец: '))
eps = float(input('Погрешность: '))

print('№\t\tНачало\t\tКонец')

while True:
  k += 1
  c = (a + b) // 2
  if (f(a) * f(c) >= 0):
    a = c
  else:
    b = c
  
  if (abs(b - a) > eps):
    print('Корень:', c)
    print('Кол-во делений: %s' % k)
    break
