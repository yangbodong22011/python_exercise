cities = {}
city_0 = {'country': 'China', 'popu': '13min', 'fact': 'good'}
city_1 = {'country': 'ina', 'popu': '13min', 'fact': 'good'}
city_2 = {'country': 'Ca', 'popu': '13min', 'fact': 'good'}

cities['0'] = city_0
cities['1'] = city_1
cities['2'] = city_2

for city_name in cities.keys():
	city_info = cities[city_name]
	print("city_info is " + city_name)
	for info,ins in city_info.items():
		print(info + ":" + ins)
