#!/usr/bin/env.exe python
#from mo import func
tp = (int, float)
tp2 = (float, str)
inp = input('input a num:')
if not isinstance(inp, tp2):		#check type
	#raise TypeError('sunqi')
	print('type error')
	pass
else:
	print('is a num')

#help(isinstance)

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print(add_end([1,2,3]))
