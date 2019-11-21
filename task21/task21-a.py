# 3

# Мышьяк

c0 = 1.5
k = 1.05
cdop = 0.05

cpred = c0

i = 1

while True:
	c = cpred / k
	print('{} сутки. Содеражние мышьяка: {}'.format(i, c))
	if c <= cdop:
		break
	cpred = c
	i += 1