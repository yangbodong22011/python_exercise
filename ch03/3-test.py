array = ['a', 'b', 'c', 'd']
print(array)
print(array[-1])
print(len(array))


array.append('e')
array.insert(0, 'f')
array.extend('g')
print(array)

array.pop()
del array[0]
array.remove('e')
print(array)

array[0] = 'x'
print(array)

index = array.index('x')
print(index)
	
array.sort()
array.sort(reverse=True)
print(array)

array.reverse()
print(array)