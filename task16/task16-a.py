#3

q = int(input('System: '))

x = input('Num: ')

l = len(x)

tenNum = 0

i = 0

c = l - 1

while c > -1:
    tenNum += int(x[i]) * q ** c
    c -= 1
    i += 1

print('\nAnswer:', tenNum)
