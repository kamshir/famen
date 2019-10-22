# 3

print('\nПервое задание\n')

side = float(input('Сторона квадрата: '))

x = float(input('x: '))
y = float(input('y: '))

if (x >= 0 and x <= side and (y == 0 or y == side)) or (y >= 0 and y <= side and (x == 0 or x == side)):
	print('Точка на стороне квадрата!')
elif x > side or x < 0:
	print('Точка за пределами квадрата!')
elif (x > 0 and x < side) and (y > 0 and y < side):
	print('Точка внутри квадрата!')


# 4

print('\nВторое задание\n')

print('Введите координаты центра бублика:')

coordX = float(input())
coordY = float(input())

rIn = float(input('Радиус внутренней окружности: '))
rOut = float(input('Радиус внешней окружности: '))

x = float(input('x: '))
y = float(input('y: '))

if (x > coordX + rOut or x < coordX - rOut) or (y > coordY + rOut or y < coordY - rOut):
	print('Точка за пределами бублика!')

elif ((x < coordX + rOut and x > coordX + rIn) or (x > coordX - rOut and x < coordX - rIn)) and ((y < coordY + rOut and y > coordY + rIn) or (y > coordY - rOut and y < coordY - rIn)):
	print('Точка на бублике')

elif (x > coordX - rIn and x < coordX + rIn) and (y > coordY - rIn and y < coordY + rIn):
	print('Точка внутри бублика')

# 5

print('\nТретье задание\n')

side = float(input('Сторона квадрата: '))

x = float(input('x: '))
y = float(input('y: '))

abroad = side - side*2

if (x > side or x < abroad) or (y > side or y < abroad):
	print('Точка за пределами границ!')

elif (x < side and x > 0) and (y < side and y > 0):
	print('Точка в 1-й четверти')

elif (x < 0 and x > abroad) and (y < side and y > 0):
	print('Точка в 2-й четверти')

elif (x < 0 and x > abroad) and (y < 0 and y > abroad):
	print('Точка в 3-й четверти')

elif (x < side and x > 0) and (y < 0 and y > abroad):
	print('Точка в 4-й четверти')