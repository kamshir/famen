# 3

print('Члены ряда, еньше eps\n')

print('-' * 30)

cnt = int(input('Кол-во чисел: '))

arr = []

c = 0

eps = float(input('Точность: '))

def factorial(a):
	n = 1
	while a > 1:
		n *= a
		a -= 1

	return n

while True:
	c += 1

	num = int(input('{} Число: '.format(c)))
	arr.append(num)

	if c == cnt:
		break

k = 0

sum = 0

print('')

for i in range(len(arr)):
	el = arr[i]
	num = (10**el) / factorial(el)

	if num < eps:
		k += 1
		sum += num
		print('{}. {}'.format(k, num))

print('\nСумма элементов, меньшк eps: {}'.format(sum))

print('\nИх количество: {}'.format(k))