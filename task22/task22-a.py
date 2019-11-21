# 3

def factorial(a):
	c = 1
	while a > 0:
		c *= a
		a -= 1

	return c

def kol_vo(n, k):
	cnt = factorial(n) // factorial(n - k)

	return cnt


# 1 example

k = 3
n = [1,2,3,4,5]
cnt = len(n)

cnt1 = kol_vo(cnt, k)

print('3-x чисел из комбинации: {}: {}'.format(n, cnt1))

# 2 example

k = 2
n = [2,4,6,8]
cnt = len(n)

cnt2 = kol_vo(cnt, k)

print('2-x чисел из комбинации: {}:    {}'.format(n, cnt2))

# 3 example

k = 4
n = [1,3,7,8,9]
cnt = len(n)

cnt3 = kol_vo(cnt, k)

print('4-x чисел из комбинации: {}: {}'.format(n, cnt3))

big = max(cnt1, cnt2, cnt3)

print('\nОтвет: ', end="")

if big == cnt1:
	print('3-х чисел больше')
elif big == cnt2:
	print('2-х чисел больше')
elif big == cnt3:
	print('4-х чисел больше')