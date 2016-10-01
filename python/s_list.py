#!/usr/bin/env.exe python
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[1], classmates[-2])

print(classmates.append('Adam'))
print(classmates)

print(classmates.insert(1, 'Jack'))
print(classmates)

print(classmates.pop(1))
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]
classmates.insert(1, L)
print(classmates)
print(classmates[1][0])

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(classmates[1])
print(type((1)), type((1, )))

L = (1,2,['1', '2'])
print(L)
L[2][1] = 'a'
print(L)

print('input your age: ')
age = int(input())
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('kid')
