class Car:
	def move(self):
		print('Car - move()')

class Toy:
	def move(self):
			print('Toy - move()')

class ToyCar(Toy, Car):
	""" A Toy Car """

tc = ToyCar()
tc.move()
