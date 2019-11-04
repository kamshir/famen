month = input('Номер месяца: ')

if month != '':
	month = int(month)
	if month >= 1 and month < 3 or month == 12:
		print('Зима')
	elif month >= 3 and month < 6:
		print('Весна')
	elif month >= 6 and month < 9:
		print('Лето')
	elif month >= 9 and month < 12:
		print('Осень')
	else:
		print('Не номер месяца')
else:
	print('Вы ничего не ввели')