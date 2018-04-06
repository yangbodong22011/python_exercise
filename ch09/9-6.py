class Restaurant():
	''' This is class of Restaurant '''
	def __init__(self, restaurant_name, cuisine_type, number_served):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		# number_served is 9.4 
		self.number_served = number_served


	def describe_resuaurant(self):
		print("name is " + self.restaurant_name)
		print("type is " + self.cuisine_type)
		# 9.4
		print("total " + str(self.number_served) + " user eat food");

	def open_resuaurant(self):
		print(self.restaurant_name + " is open")

	# 9.4
	def set_number_served(self, number_served):
		self.number_served = number_served

	# 9.4
	def increment_number_served(self, increment_number_served):
		self.number_served += increment_number_served

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type, number_served, flavors):
		super().__init__(restaurant_name, cuisine_type, number_served)
		self.flavors = flavors

	def show_all(self):
		for ice in self.flavors:
			print(ice)

flavors = ['a', 'b', 'c']
ice = IceCreamStand("aaa", "bbb", "ccc", flavors)
ice.show_all()
ice.describe_resuaurant()