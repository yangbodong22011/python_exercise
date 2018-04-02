friend = {
	'first_name': 'yang',
	'last_name': 'bodong',
	'age': 22,
	'city': 'hangzhou'
}

print(friend)

favouite_num = {
	'tom': 4,
	'danny': 5
}

print("tom like : " + str(favouite_num['tom']))
print("danny like : " + str(favouite_num['danny']))

program = {'c++':"aaa", 'java':"bbb", 'python':"good"}
print(program)

for lan,des in program.items():
	print(lan + " : " + des)