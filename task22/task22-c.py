# 5

def factorial(a):
	c = 1
	while a > 0:
		c *= a
		a -= 1

	return c

def team(k, n):
	cnt = factorial(n) // (factorial(k) * factorial(n - k))

	return cnt

def findEps(n, k, r, s):
	eps = (team(s, k) * team(r-s, n-k)) / team(r, n)

	return eps

# 1 var
n = 10
k = 5
r= 4
s = 2

print('1) n = {}, k = {}, r = {}, s = {}'.format(n,k,r,s))

eps1 = round(findEps(n, k, r, s), 5)

print('Вероятность: {}'.format(eps1))

# 2 var
n = 10
k = 4
r= 5
s = 3

print('\n2) n = {}, k = {}, r = {}, s = {}'.format(n,k,r,s))

eps2 = round(findEps(n, k, r, s), 5)

print('Вероятность: {}'.format(eps2))