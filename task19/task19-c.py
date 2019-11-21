# 5

from random import randint

print('№\t|Январь |Февраль|  Март |Апрель |  Май  |  Июнь |  Июль | Август|Сентябрь|Октябрь|Ноябрь |Декабрь|Сред.зарпл.|Зарпл. за год|')
print('-'*132)

sumProfit = 0
averProfit = 0

for i in range(12):
	stroka = str(i+1)
	summa = 0
	for i in range(12):
		profit = randint(1000, 5000)
		if i > 8:
			stroka += '\t |${}'.format(profit)
		else:
			stroka += '\t|${}'.format(profit)
		summa += profit

	aver = summa // 12
	averProfit += aver
	stroka += '\t |   ${}   |    ${}   |'.format(aver, summa)
	sumProfit += summa
	print(stroka)

averProfit //= 12

print('\nСуммарная зарплата по фирме за год: ${}'.format(sumProfit))
print('Средняя зарплата по фирме за гож: ${}'.format(averProfit))