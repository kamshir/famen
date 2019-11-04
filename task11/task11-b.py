years = input('Введите количество лет от 1 до 99: ')

if years != '':
	years = int(years)
	if years >= 1 and years < 100:
		end = years % 10
		if years >= 11 and years < 21:
			age = 'лет'
		elif end == 1:
			age = 'год'
		elif end >= 2 and end < 5:
			age = 'года'
		else:
			age = 'лет'

		print('Мне {} {}'.format(years, age))

	else:
		print('Вы ввели число вне диапозона')

else:
	print('Вы ничего не ввели')