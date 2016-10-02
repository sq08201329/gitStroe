#!/usr/bin/env.exe python
#from mo import func
tp = (int, float)
inp = input()
if not isinstance(inp, tp):		#check type
	raise TypeError('sunqi')
