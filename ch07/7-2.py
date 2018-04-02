# sum = 0;
# for i in range(1, 10):
# 	sum += i
# print(sum)

# peiliao = ""

# while peiliao != "quit":
# 	peiliao = input("input:")
# 	print("we will add " + str(peiliao))

age = 0;
const = 0
while True:
	age = input("input age")
	if age > 0 and age < 3:
		const = 0
	elif age >= 3 and age < 12:
		const = 10
	elif age >= 12:
		const = 15
	print("we will const $" + str(const))	
