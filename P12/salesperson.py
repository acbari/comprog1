from person import Person
from employee import Employee

class SalesPerson(Employee):
	def __init__(self, name, age, id, region, sales):
		super().__init__(name, age, id)
		self.region = region
		self.sales = sales
		
	def bonus(self):
		return self.sales * 0.5

if __name__ == "__main__":
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