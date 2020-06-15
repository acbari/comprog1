class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def birthday(self):
		print ('Happy birthday you were', self.age)
		self.age += 1
		print('You are now', self.age)

class Employee(Person):
	def __init__(self, name, age, id):
		super().__init__(name, age)
		self.id = id

	def calculate_pay(self, hours_worked):
		rate_of_pay = 7.50
		if self.age >= 21:
			rate_of_pay += 2.50
		return hours_worked * rate_of_pay
	
class SalesPerson(Employee):
	def __init__(self, name, age, id, region, sales):
		super().__init__(name, age, id)
		self.region = region
		self.sales = sales
		
	def bonus(self):
		return self.sales * 0.5

if __name__ == "__main__":
	e = Employee('Denise', 51, 7468)
	p = Person('John', 54)
	print(p.calculate_pay(10))
	"""
	print('-'*10)
	print('Person:')
	p = Person('John', 54)
	print(p.name+' is '+str(p.age))
	print('-'*10)

	print('Employee:')
	e = Employee('Denise', 51, 7468)
	print(e.name+' id: '+str(e.id))
	e.birthday()
	print(e.name+' is'+str(e.age))
	print('Payment (40 hour): ', e.calculate_pay(40))
	print('-'*10)
	
	s = SalesPerson('Phoebe', 21,4712, 'UK', 30000.0)
	print(s.name +' is'+str(s.age))
	s.birthday()
	print('s.calculate_pay(40):', s.calculate_pay(40))
	print('s.bonus():', s.bonus())
	"""