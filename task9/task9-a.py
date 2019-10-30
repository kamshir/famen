# 3 

class Ticket:
  def __init__(self):
    self.ticket = int(input('Введите билет: '))

  def is_lucky(self):
    t = self.ticket
    length = len(str(t))
    div = int('1' + ((length // 2) * "0"))
    fhalf = t // div
    shalf = t % div

    fsum, ssum = list(), list()
    for i in range(length // 2):
      fsum.append(int(str(fhalf)[i]))
      ssum.append(int(str(shalf)[i]))

    if (sum(fsum) == sum(ssum)):
      print('Билет счастливый!')
    else:
      print('Обычный билет')

ticket = Ticket()
ticket.is_lucky()