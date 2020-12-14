#!/usr/bin/python3
#				"Quadratic equation"
import cmath
#	y = ax^2 + bx + c
a = 1
b = 5
c = 6
delta = b**2 - 4*a*c
if delta<0:	
	print('This equation doesnt have roots')
elif delta==0:
	x0 = -b/(2*a)
	print('There is one root: '+ x0)
else:
	x1 = (-b-cmath.sqrt(delta))/(2*a)
	x2 = (-b+cmath.sqrt(delta))/(2*a)
	print('There are two roots: {0} and {1}'.format(x1,x2))
