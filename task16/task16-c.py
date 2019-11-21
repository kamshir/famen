# 5

q1 = int(input('Исх. Сист. Счисления: '))
q2 = int(input('Желаемая Сист. Счисления: '))
num = input('Число системы q1: ')

print('\nПеревод в q2:')
print('-'*30)

# Перевод в 10-ю
tenNum = 0

i = 0

c = len(num) - 1

while c > -1:
    tenNum += int(num[i]) * q1 ** c
    c -= 1
    i += 1

# Перевод в q2

num = ''

while tenNum > 0:
	n = tenNum % q2
	tenNum = tenNum // q2
	num += str(n)

num = num[::-1]

print('Ответ:',num)