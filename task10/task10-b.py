# 4
bookprice = float(input('Введите стоимость книг: '))

cash = float(input('Введите сумму денег, внесённую покупателем: '))

if bookprice == cash:
  print('Спасибо за покупку. И спасибо, что без сдачи.')
elif bookprice < cash:
  forward = cash - bookprice
  print('Возьмите сдачу: {}'.format(forward))
else:
  less = bookprice - cash
  print('Вам не хватает: {}'.format(less))
