#3
# pays from 5000 to 20000
from random import randint

prozhMin = int(input('Прожиточный минимум работника: '))

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
summa = 0
biggest, smallest = 4999, 21000
bigMonth, smallMonth = 0, 0
sumPens = 0
nalogi = 0
count = 0
sumItog = 0

print('Месяц \t\tЗарплата \tПенс.фонд \tПр.Мин \t\tПод.Налог \tИтог')
print('-'*100)

for i in range(len(months)):
	month = months[i]
	cash = randint(5000, 20000)
	summa += cash
	if cash >= biggest:
		biggest = cash
		bigMonth = month
	if cash <= smallest:
		smallest = cash
		smallMonth = month

	#5
	pens = cash // 100 * 2
	sumPens += pens
	if cash > prozhMin:
		prozh = '+'
	else:
		prozh = '-'
		count += 1

	if summa > 20000:
		nalog = int(cash * 0.13)
	else:
		nalog = 0

	nalogi += nalog
	itog = cash - nalog - pens
	sumItog += itog

	if i > 1 and i <=7 or i == 0 or i == 10:
		print('{} \t\t {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(month, cash, pens, prozh, nalog, itog))
	else:
		print('{} \t {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(month, cash, pens, prozh, nalog, itog))

print('-'*100)

average = round(summa / len(months), 2)
print('Всего: \t\t', summa,'\t', sumPens, '\t', '\t{} мес.'.format(count), '\t', nalogi, '\t\t', sumItog)
print('')

print('Средняя зарплата сотрудника:', average)
print('')
print('Наибольшая зарплата: {}.\nПолучена в {}.\n'.format(biggest, bigMonth))
print('Наименьшая зарплата: {}.\nПолучена в {}.\n'.format(smallest, smallMonth))

#4

