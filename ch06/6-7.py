# friend_1 = {
# 	'first_name': 'yang',
# 	'last_name': 'bodong',
# 	'age': 22,
# 	'city': 'hangzhou'
# }

# friend_2 = {
# 	'first_name': 'yang',
# 	'last_name': 'bodong',
# 	'age': 22,
# 	'city': 'hangzhou'
# }

# friend_3 = {
# 	'first_name': 'yang',
# 	'last_name': 'bodong',
# 	'age': 22,
# 	'city': 'hangzhou'
# }

# friends = [friend_1, friend_2, friend_3]

# for f in friends:
# 	print(f['first_name'] + ":" + f['last_name'] + ":" + str(f['age']) + ":" + f['city'])


place_1 = ['aaa', 'bbb', 'ccc']
place_2 = ['ddd', 'eee', 'fff']
place_3 = ['ggg', 'hhh', 'iii']
favouite_places = {}
favouite_places['danny'] = place_1
favouite_places['janny'] = place_2
favouite_places['tom'] = place_3

for name,place in favouite_places.items():
	print(name + "is like")
	for p in place:
		print(p)
	print("...")
	



