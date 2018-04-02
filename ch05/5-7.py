fruits = ["apple", "pear", "banana", "peach"]
if "apple" in fruits:
	print("I really like apple")
if "pear" in fruits:
	print("I really like pear");
if "xxx" not in fruits:
	print("xxx not in fruits")

requested_toppings = ['mashrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("sorry")
	else:
		print("add " + requested_topping + ".")