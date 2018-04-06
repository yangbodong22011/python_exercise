class User():
	''' Describe all user'''

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		print("Hello, I am " + self.first_name.title() + " " +
			self.last_name)
		print("I was login attempts: " + str(self.login_attempts))

	def greet_user(self):
		print("Hello, " + self.first_name + " " + self.last_name
			+ ", Good Monring");

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

# user_1 = User("yang", "bodong")
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User("zhang", "wei")
# user_2.describe_user()
# user_2.greet_user()


# 9-5
user_3 = User("zhang", "weida")
user_3.describe_user()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.describe_user()
user_3.reset_login_attempts()
user_3.describe_user()
