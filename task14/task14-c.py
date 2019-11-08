# 5

neededHarvest = float(input('Введите желаемый объем урожая: '))

year = 1

square = 100

productivity = 20

harvest = square * productivity

print('Год\t', 'Объём урожая\t', 'Урожайность\t', 'Площадь')
print('-'*50) 

while harvest <= neededHarvest:
	if year == 1:
		print(' {} \t  {} \t\t  {} \t\t  {}'.format(year, harvest, productivity, square))
		print('-'*50) 

	year += 1
	square = round(square + square * 0.05, 2)
	productivity = round(productivity + productivity * 0.02, 2)
	harvest = round(square * productivity, 2)

	if year == 2 or year == 10 or year == 15:
		print(' {} \t  {} \t  {} \t\t  {}'.format(year, harvest, productivity, square))
	else:
		print(' {} \t  {} \t  {} \t  {}'.format(year, harvest, productivity, square))
	print('-'*50) 

print('Потребовалось {} лет'.format(year))