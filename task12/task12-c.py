#5

count = int(input('Kol-vo chisel: '))

summa = 0

big = -1024**1023

small = 1024**1024

posMax, posMin = 0, 0

for i in range(1, count + 1):
	el = int(input('{} element: '.format(i)))
	if el >= big:
		big = el
		posMax = i
	if el <= small:
		small = el
		posMin = i

	summa += el

print('-'*30)

print('\nSum:', summa)

print('max:', big)
print('Reach in position', posMax)

print('min:', small)
print('Reach in position', posMin)
