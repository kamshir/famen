# 3
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = int(input('Введите d: '))

if a == d:
  print('a == d')
elif b == d:
  print('b == d')
elif c == d:
  print('c == d')
else:
  ar = ['d-a', 'd-b', 'd-c']
  ar2 = []
  for i in range(len(ar)):
    ar2.append(eval(ar[i]))
  big = max(ar2)
  for i in range(len(ar)):
    if big == ar2[i]:
      print("Максимальное: {} = {}".format(str(ar[i]), big))
