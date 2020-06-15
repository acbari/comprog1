class Bear:
	def sound(self):
		print("Groarrr")
    
class Dog:
	def giveName(self, name):
		self.name = name
		
	def sound(self):
		print("Woof woof!")
    
def makeSound(animalType):
	animalType.sound()
	print("<end of sound>")


honeyBear = Bear()
bullDog = Dog()
bullDog.giveName("Buddy")
    
makeSound(honeyBear)
makeSound(bullDog)

Animals = [honeyBear, bullDog]
print("Animals:",Animals)
for animal in Animals:
	print(animal)
	print(makeSound(animal))
print("Animals:",Animals)