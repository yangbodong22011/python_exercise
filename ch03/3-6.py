names = ['a', 'b', 'c']
print("i wanna eat dinna with you, " + names[0])
print("i wanna eat dinna with you, " + names[1])
print("i wanna eat dinna with you, " + names[2])
print("could not attent: " + names[0]);
names[0] = 'e';
print("i wanna eat dinna with you, " + names[0]);
print("i wanna eat dinna with you, " + names[1])
print("i wanna eat dinna with you, " + names[2])
print("i find a big table")
names.insert(0, 'f')
names_len = len(names)
half = names_len/2
names.insert(int(half), 'g')
names.insert(-1, 'h')


print("i wanna eat dinna with you, " + names[0]);
print("i wanna eat dinna with you, " + names[1])
print("i wanna eat dinna with you, " + names[2])
print("i wanna eat dinna with you, " + names[3]);
print("i wanna eat dinna with you, " + names[4])
print("i wanna eat dinna with you, " + names[5])

print("sorry, i just can invite two")

print(names.pop() + ", i am sorry")
print(names.pop() + ", i am sorry")
print(names.pop() + ", i am sorry")
print(names.pop() + ", i am sorry")

print(names[0] + ", you also in table")
print(names[1] + ", you also in table")
print(names)

del names[1]
del names[0]

print(names)

