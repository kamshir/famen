# 4

fishes = int(input('Введите количество рыбок в аквариуме: '))
catch = 7.00
time = 0

while fishes > 0:
	print('{} рыба, время: {}'.format(fishes, round(catch, 2)))
	fishes -= 1
	catch += catch * 0.05
	time += catch

print('Такое количество рыбок мальчик переложит в банку за {} сек.'.format(round(time, 2)))