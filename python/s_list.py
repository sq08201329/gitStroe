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

print()
i = 0
for name in classmates:
	i = i + 1
	print(i,': ',name)

sum = 0
for x in range(101):
	if x > 10:
		break
	sum = sum + x
	print(x)
print(sum)

n = 0
while n < 10:
	n = n + 1
	if n%2 == 0:
		continue
	print(n)

d={}
print('input students fenshu:')
i = 0
for name in classmates:
	print(name,'\'s fenshu')
	fenshu = int(input())
	d[name] = fenshu

print(d)

print(d.pop('Bob'))
print(d)


s = set([1,2,2,2,3,4,3,4])
print(s)
s.add(4)
print(s)

l1 = [1,2,3]
l2 = [2,3,4]
s1 = set(l1)
s2 = set(l2)
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)	#in s1 not in s2
print(s2 - s1)	#in s1 not in s2
print(s1 ^ s2)	#in s1 or in s2,but not in s1 & s2
print((s1 | s2) - (s1 & s2))
