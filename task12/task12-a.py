#3
number = int(input('Enter the numb: '))

f = 1

for i in range(1, number + 1):
	f = f * i

print('{}! = {}'.format(number, f))
