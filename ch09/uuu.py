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

class Privileges():
	def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
		self.privileges = privileges
	def show_admin_privileges(self):
		for privilege in self.privileges:
			print(privilege)

class Admin(User):

	def __init__(self, first_name, last_name, privileges=Privileges()):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()