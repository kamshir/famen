# 5

q1 = int(input('Исходная система счисления: '))

num = input('Число в этой системе: ')

q2 = int(input('В какую перевести?: '))

l = len(num)

tenNum = 0

i = 0

c = l - 1

while c > -1:

    tenNum += int(num[i]) * q1 ** c

    c -= 1

    i += 1

returnNum = ''

num = int(num)

while num > 0:
  dif = num % q2
  num = num // q2
  returnNum += str(dif)

returnNum = returnNum[::-1]

print(returnNum)
