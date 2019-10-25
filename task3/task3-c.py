# 5

class Trapezoid:
	def __init__(self, lb, ls, h):
		self.lenBig = lb
		self.lenSmall = ls
		self.height = h

	def square(self):

		square = 0.5 * (self.lenSmall + self.lenBig) * self.height

		return square 

lenBig = float(input('Введите длину большего основания: '))

lenSmall = float(input('Введите длину меньшего основания: '))

height = float(input('Введите длину высоты: '))

trapez = Trapezoid(lenBig, lenSmall, height)

square = trapez.square()

print('\nПлощадь трапеции: {}'.format(square))