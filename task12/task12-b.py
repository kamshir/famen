#4

count = int(input('Kol-vo chisel: '))

summa = 0

big = -1024**1023

small = 1024**1024

for i in range(1, count + 1):
	el = int(input('{} element: '.format(i)))
	if el >= big:
		big = el
	if el <= small:
		small = el

	summa += el

print('-'*30)

print('\nSum:', summa)

print('max:', big)

print('min:', small)
