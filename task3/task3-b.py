# 4 
from math import pi

class Ring:
	def __init__(self, rb, rs):
		self.rIn = rs
		self.rOut = rb

	def square(self):
		sSmall = 2 * pi * rIn**2
		sBig = 2 * pi * rOut**2

		sAll = sBig - sSmall

		return sAll 

rOut = float(input('Введите радис внешнего круга: '))

rIn = float(input('Введите радис внутреннего круга: '))

ring = Ring(rOut, rIn)

square = ring.square()

print('\nПлощадь кольца: {}'.format(round(square, 2)))