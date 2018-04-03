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

# my_re = Restaurant("grand mother", "chaocai")
# my_re.describe_resuaurant()
# my_re.open_resuaurant()

# my_re2 = Restaurant("chaotianmen", "huoguo")
# my_re2.describe_resuaurant()


# my_re3 = Restaurant("maidanglao", "hanbao")
# my_re3.describe_resuaurant()
# error 
# 1. 函数加def
# 2. 只有_init__需要传递所有参数



# 9.4
my_re4 = Restaurant("maidanglao", "fastfood", 100)
my_re4.set_number_served(2000)
my_re4.increment_number_served(100)
my_re4.describe_resuaurant()

