# 3

laps = 64 

rabbits = laps // 4
ducks = 0

print('гуси\tкролики')
print(ducks, '\t',rabbits)

while rabbits > 0:
	rabbits -= 1
	ducks += 2

	print(ducks, '\t',rabbits)