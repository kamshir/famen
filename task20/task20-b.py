# 4

s = int(input('Введите сумму в копейках: '))

print('Варианты сдачи:')
print('-'*25)

print('2 коп.\t5 коп.\t10 коп.')

print('-'*25)

k10 = s // 10

if s % 10 == 0:
	print('{} \t {} \t {}'.format(0, 0, k10))
	k5 = 0
	while True:
		k10 -= 1
		k5 += 2
		print('{} \t {} \t {}'.format(0, k5, k10))
		if k10 == 0:
			break

	k10 = s // 10
	k2 = 5
	k5 = -2
	while k10 > 0:
		k10 -= 1
		k5 += 2
		print('{} \t {} \t {}'.format(k2, k5, k10))

	while k5 > 0:
		k5 -= 2
		k2 += 5
		print('{} \t {} \t {}'.format(k2, k5, k10))

else:
	os10 = s % 10
	if os10 >= 5 and os10 % 2 == 1:
		k5 = -1
		k2 = (os10-5) // 2
		while k10 >= 0:
			k5 += 2
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k10 == 0:
				break
			k10 -= 1

		k5 -= 2
		while k5 >= 1:
			k2 += 5
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k5 == 1:
				break
			k5 -= 2

	elif os10 >= 5 and os10 % 2 == 0:
		k2 = os10 // 2
		k5 = -2
		while k10 >= 0:
			k5 += 2
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k10 == 0:
				break
			k10 -= 1

		k5 -= 2
		while k5 >= 0:
			k2 += 5
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k5 == 0:
				break
			k5 -= 2

	elif os10 < 5 and os10 % 2 == 1:
		k10 -= 1
		k5 = -1
		k2 = (s - 5) % 10 // 2
		while k10 >= 0:
			k5 += 2
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k10 == 0:
				break
			k10 -= 1

		k5 -= 2
		while k5 >= 1:
			k2 += 5
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k5 == 1:
				break
			k5 -= 2

	elif os10 < 5 and os10 % 2 == 0:
		k2 = os10 // 2
		k5 = -2
		while k10 >= 0:
			k5 += 2
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k10 == 0:
				break
			k10 -= 1

		k5 -= 2
		while k5 >= 0:
			k2 += 5
			print('{} \t {} \t {}'.format(k2, k5, k10))
			if k5 == 0:
				break
			k5 -= 2