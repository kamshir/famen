# 5

class Time:
	def __init__(self):
		self.sec = int(input('Введите количество секунд: '))

	def fullTime(self):
		hours = self.sec // 3600
		minutes = self.sec % 3600 // 60
		seconds = self.sec % 3600 % 60

		time = "Время: {}:{}:{}".format(hours, minutes, seconds)

		return time


seconds = Time()

time = seconds.fullTime()

print(time)