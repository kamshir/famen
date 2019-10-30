# 5
from itertools import permutations

class Number:
  def __init__(self):
    self.number = int(input('Введите число: '))

  def shufle(self):
    biggest = 0
    n = self.number
    digs = []
    length = len(str(n))
    for i in range(length):
      digs.append(int(str(n)[i]))

    count = list(permutations(digs))

    print('Варианты чисел:')
    for i in range(len(count)):
      c = list(count[i])
      ar = []
      for j in range(len(c)):
        ar.append(str(c[j]))

      num = int(''.join(ar))

      if num > biggest:
        biggest = num

      print('{}.\t{}'.format(i+1, num))

    print('Наибольшее: {}'.format(biggest))

number = Number()

number.shufle()