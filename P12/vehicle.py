class Vehicle:
	def __init__(self, num_of_wheels, engine_type, fuel_capacity, seats, max_velocity):
		self.wheels = num_of_wheels
		self.engine_type = engine_type
		self.fuel_capacity = fuel_capacity
		self.seats = seats
		self.max_velocity = max_velocity

	def get_fuel_capacity(self):
		return self.fuel_capacity

	def add_fuel_capacity(self, extra_capacity):
		self.fuel_capacity += extra_capacity

if __name__ == "__main__":
	tesla_model_s = Vehicle(4, 'electric', 70, 5, 250)
	tesla_model_s.add_fuel_capacity(30)
	print(tesla_model_s.get_fuel_capacity())

