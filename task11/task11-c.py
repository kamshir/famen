class Data:
	def __init__(self):
		self.data = input('Введите дату в виде [dd mm yyyy]: ').strip()
		while len(self.data) != 10:
			print('\nВведите дату правильно!\n')
			self.data = input('Введите дату в виде [dd mm yyyy]: ').strip()

	def getDay(self):
		days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
		d = self.data
		day = int(d[0:2])
		month = int(d[3:5]) - 2
		year = int(d[6:])
	
		def dayForm():
			c = int(str(year)[0:2])
			y = int(str(year)[2:])
			x = int(2.6*month - 0.2) + day + int(y / 4) + y + int(c / 4) - 2*c
			df = x % 7

			return df

		if year >= 1582 and year < 4903:
			dayOfWeek = dayForm()
			print('Это:', days[dayOfWeek])
		else:
			print('\nВы ввели слишком большой/маленький год\n')
			year = input('Введите год от 1582 до 4902: ')
			while len(year) != 4:
				print('\nНеправильно!\n')
				year = input('Введите год от 1582 до 4902: ')
			year = int(year)
			while year < 1582 or year > 4902:
				print('\nНеверно\n')
				year = int(input('Введите год от 1582 до 4902: '))
			dayOfWeek = dayForm()
			print('Это:', days[dayOfWeek])


data = Data()
data.getDay()
