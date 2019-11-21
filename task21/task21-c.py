# 5

# Любое вещество (свинец например)

c0 = float(input('Сод. вещ-ва: '))
k = float(input('Коэффициент: '))
cdop = float(input('Сдоп (мг/л): '))

cpred = c0

i = 1

while True:
	c = cpred / k
	print('{} сутки. Содеражние фтора: {}'.format(i, c))
	if c <= cdop:
		break
	cpred = c
	i += 1