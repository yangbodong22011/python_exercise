def get_list_intersection(list_1, list_2):
	return_list = []
	for i in list_1:
		for j in list_2:
			if i == j:
				return_list.append(i)
	return return_list

list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
print(get_list_intersection(list_1, list_2))

