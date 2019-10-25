# 4

class Select:
	def __init__(self):
		self.man = int(input('Возраст мужчины: '))
		self.woman = int(input('Возраст женщины: '))

	def girlForMan(self):
		woman = self.man // 2 + 7

		return woman

	def manForGirl(self):
		man = self.woman * 2 - 17

		return man

selection = Select()

girlToMan = selection.girlForMan()

manToGirl = selection.manForGirl()

print('\nВозраст женщины: {}'.format(girlToMan))
print('\nВозраст мужчины: {}'.format(manToGirl))