# users = ['tom', 'danny', 'liming', 'jack', 'admin']
# users = []
# if users:
# 	for user in users:
# 		if user == "admin":
# 			print("hello,"+ user + ",see a report.")
# 		else:
# 			print("hello,"+ user + ",welcome.")
# else:
# 	print("we need users")

# current_users = ['tom', 'danny', 'liming', 'jack', 'admin']
# new_users = ['tom', 'abc', 'Danny', "dcc", "fds"]

# for new_user in new_users:
# 	if new_user.lower() in current_users:
# 		print("This name is used " + new_user)
# 	else:
# 		print("This name can be use " + new_user)

nums = list(range(1,10))
for num in nums:
	if num == 1:
		print(str(num) + "st")
	elif num == 2:
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "th")