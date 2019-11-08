# 3
words = 5
end = 250
count = words
days = 1

while count <= end:
	if days == 1:
		print('{} день - {} слов. Словарный запас {}'.format(days, words, count))

	words += 2
	count += words
	days += 1
	print('{} день - {} слов. Словарный запас {}'.format(days, words, count))

print('Ответ: За {} дней'.format(days))