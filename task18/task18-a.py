# 3

print('Члены ряда 10n-5')

print('-' * 30)

cnt = int(input('Кол-во чисел: '))

arr = []

c = 0

comp = 10**-5

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

print('')

for i in arr:
	num = (10**i) / factorial(i)

	if num >= comp:
		k += 1
		print('{}. {}'.format(k, num))

print('Их количество: {}'.format(k))