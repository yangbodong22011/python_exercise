from random import randint

class Die():

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print("The answer is " + str(randint(1,6)))

die = Die()
for i in range(1, 11):
	die.roll_die()