# 4

x = int(input('Введите число в 10-й чистеме счисления: '))

q = int(input('Выберите нужную систему счисления: '))

returnNum = ''

while x > 0:
  dif = x % q
  x = x // q
  returnNum += str(dif)

returnNum = returnNum[::-1]

print(returnNum)
