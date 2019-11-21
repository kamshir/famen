# 3

from random import randint

print('№\t|Январь |Февраль|  Март |Апрель |  Май  |  Июнь |  Июль | Август|Сентябрь|Октябрь|Ноябрь |Декабрь|Зарп. за год|')
print('-'*119)

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

	stroka += '\t |  ${}    |'.format(summa)
	print(stroka)