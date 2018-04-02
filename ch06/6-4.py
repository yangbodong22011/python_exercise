# program = {'c++':"aaa", 'java':"bbb", 'python':"good"}

# for k,v in program.items():
# 	print(k + ":" + v)

# program['c'] = 'very good'
# program['go'] = 'gc'

# for k,v in program.items():
# 	print(k + ":" + v)

river = {
	'nile': 'egypt',
	'huanghe': 'China',
	'changjiang': 'China'
}

print(river)

for river_name, country in river.items():
	print("The " + river_name + " runs through " + country)

for river_name in river.keys():
	print(river_name)

for country in river.values():
	print(country)


r = ['nile', 'huanghe', 'changjiang', 'niluohe']

for rs in r:
	if rs in river.keys():
		print(rs + " is in")
	else:
		print(rs + " not in")