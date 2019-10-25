# задание на 5

class Test:

	def __init__(self):
		print('\nТест был успешно создан!\n')
		self.grade = 0
		self.answers = ['A', 'D', 'C', 'D', 'C']
		self.userAnswers = list()
		self.questions = [
						  ['Какой язык является статически типизированным?', ['A. C++', 'B. Python', 'C. JavaScript', 'D. 1C']], 
						  ['Что из списка не является текстовым редактором?', ['A. Блокнот', 'B. Notepad++', 'C. Visual Studio Code', 'D. Visual Basic']],
						  ['Что такое Linux?', ['A. Известная компания', 'B. Древнегреческое имя', 'C. Операционная система', 'D. Марка компьютера']],
						  ['Какую программу запускают новички в любом языке программирования?', ['A. Компьютерная игра', 'B. Нейронная сеть', 'C. Сбор паролей из Пентагона', 'D. "Hello world!"']],
						  ['Кто такие программисты?', ['A. Большой - большой секрет! Тщщщщ...', 'B. Люди, которые чинят бабушкам их кампуктеры', 'C. Люди, которые пишут программы на любых языках программирования', 'D. Люди, которые пишут на HTML']]
						 ]

	def goTest(self):
		print('\nНачали!\n')
		for i in range(len(self.questions)):
			quest = self.questions[i]
			print('{}. {}\n'.format(i+1, quest[0]))
			for j in quest[1]:
				print('{}'.format(j))

			answer = input('Ответ: ')

			while len(answer) != 1:
				print('\nВведи букву ответа!')
				answer = input('Ответ: ')
			print()
			if answer.upper() == self.answers[i]:
				print('\nМолодец!\n')
				self.grade += 1
			else:
				print('\nПлохо!\n')

			self.userAnswers.append(answer)

		print()
		print('№', '\tВаш\tВерный')
		for i in range(len(self.questions)):
			print(i+1, '\t{}'.format(self.userAnswers[i].upper()), '\t{}'.format(self.answers[i]))

		print('\nОценка: {} из {}\n'.format(self.grade, len(self.questions)))
		
		if self.grade <= 2:
			print('Неудовлетворительно!')
		elif self.grade == 3:
			print('Удовлетворительно!')
		elif self.grade == 4:
			print('Хорошо!')
		elif self.grade == 5:
			print('Отлично!')

test = Test()
test.goTest()