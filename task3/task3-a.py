# 3 

class Cube:
	def __init__(self, s):
		self.side = s

	def squareSides(self):
		square = self.side**2 * 6

		return square

	def volume(self):

		return self.side**3

side = float(input('Введите сторону куба: '))

cube = Cube(side)

square = cube.squareSides()

print('\nПлощадь боковых сторон: {}'.format(square))

volume = cube.volume()

print('\nОбъём куба: {}'.format(volume))