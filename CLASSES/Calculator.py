#!/usr/bin/python3
#				"Calculator"
from Complex_numbers import ComplexNumber
eq = "x + y - z"
x=ComplexNumber(2,2)
y=ComplexNumber(1,4)
z=ComplexNumber(3,5)
eval(eq).print()

print('Check: ')
print('x= ')
x.print()
print('y= ')
y.print()
print('z= ')
z.print()
sum=x+y
sum.print()
diff=sum-z
diff.print()