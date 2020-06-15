class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def birthday(self):
		print ('Happy birthday you were', self.age)
		self.age += 1
		print('You are now', self.age)
