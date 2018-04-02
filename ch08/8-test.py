def switcher(choice):
	case = ""
	if choice.islower():
		case = "lower"
	elif choice.isupper():
		case = "upper"
	elif choice.isdigit():
		case = "digit"
	switcher_dict = {
		'lower': 'lowercase letter',
		'upper': 'uppercase letter',
		'digit': 'digit letter'
	}
	return switcher_dict.get(case, "others")

print(switcher('a'))
print(switcher('A'))
print(switcher('2'))