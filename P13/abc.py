from abc import ABCMeta

class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        print('Happy Birthday')
    
class Employee(object):
    def __init__(self, name, age, id):
        self.name = name
        self.id = id
        
    def birthday(self):
        print('Its your birthday')
		
print(issubclass(Employee, Person))
e = Employee('Megan', 21, 'MS123')
print(isinstance(e, Person))

Person.register(Employee)
print(issubclass(Employee, Person))
e2 = Employee('Megan', 21, 'MS123')
print(isinstance(e2, Person))