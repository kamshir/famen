# 4

def factorial(a):
	c = 1
	while a > 0:
		c *= a
		a -= 1

	return c

def team(k, n):
	cnt = factorial(n) // (factorial(k) * factorial(n - k))

	return cnt

people = 5
# 8
candidats = 8

cnt1 = team(people, candidats)

print('Из 8 кандидатов: {}'.format(cnt1))

# 10
candidats = 10

cnt2 = team(people, candidats)

print('Из 10 кандидатов: {}'.format(cnt2))

# 11
candidats = 11

cnt3 = team(people, candidats)

print('Из 11 кандидатов: {}'.format(cnt3))