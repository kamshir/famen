# 5
minutes = float(input('Введите количество минут: '))

pay = 0

if minutes <= 50:
  pay = minutes
elif minutes > 50 and minutes <= 80:
  pay = 50 + (minutes - 50) * 0.8
elif minutes > 80 and minutes <= 100:
  pay = 74 + (minutes - 80) * 0.5
elif minutes > 100:
  pay = 84 + (minutes - 100) * 0.3

rubles = int(pay)
copeys = int(pay * 100 % 100)
print('Ваша плата за разговор: {} руб. {} копеек'.format(rubles, copeys))
