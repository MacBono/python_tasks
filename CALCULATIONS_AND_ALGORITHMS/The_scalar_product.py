#!/usr/bin/python3
#				"The scalar product"
import numpy as np
a = [1,2,12,4]
b = [2,4,2,8]
product = 0
for i in range(len(a)):
	product+=a[i]*b[i]
print(product)
print("Verification: ",np.dot(a,b))