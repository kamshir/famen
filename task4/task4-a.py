# 3

class Child:
	def __init__(self):
		self.papa = float(input('Рост папы: '))
		self.mama = float(input('Рост мамы: '))
		self.averAge = (self.papa + self.mama) / 2

	def boyHeight(self):

		boy = self.averAge + 6.4

		return boy

	def girlheight(self):

		girl = self.averAge - 6.4

		return girl

childHeight = Child()

boyHeight = childHeight.boyHeight()

girlheight = childHeight.girlheight()

print('\nРост мальчика: {}'.format(boyHeight))
print('\nРост девочки: {}'.format(girlheight))