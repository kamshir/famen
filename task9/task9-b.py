# 4
class Number:
  def __init__(self):
    self.number = int(input('Введите число: '))

  def is_palindrom(self):
    n = self.number
    rev = int(str(n)[::-1])

    if (n == rev):
      print('Перевёртыш!')
    else:
      print('Обычное число!')


number = Number()
number.is_palindrom()