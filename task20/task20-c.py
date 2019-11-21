# 5

money = 1770
horsePrice = 21
bullPrice = 31

i = 1

print('Лошади\tБыки')

while i * bullPrice < money:
	if (money - i * bullPrice) % horsePrice == 0:
		print('{} \t {}'.format(i, (money - i * bullPrice) // horsePrice))
	i += 1