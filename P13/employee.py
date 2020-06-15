from person import Person

class Employee(Person):
	def __init__(self, name, age, id):
		super().__init__(name, age)
		self.id = id

	def calculate_pay(self, hours_worked):
		rate_of_pay = 7.50
		if self.age >= 21:
			rate_of_pay += 2.50
		return hours_worked * rate_of_pay