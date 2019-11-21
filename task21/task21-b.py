# 4

# Фтор

c0 = 0.2
k = 1.01
cdop = 0.05

cpred = c0

i = 1

while True:
	c = cpred / k
	print('{} сутки. Содеражние фтора: {}'.format(i, c))
	if c <= cdop:
		break
	cpred = c
	i += 1