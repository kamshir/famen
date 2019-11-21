# 4

x = int(input('Введите число в 10-й системе счисления: '))

q = int(input('Введите систему, в которую хотите перевести: '))

num = ''

while x > 0:
	n = x%q
	x = x // q
	num += str(n)

num = num[::-1]

l = len(num)

print('-'*30)

print('Готовое число:', fpart)