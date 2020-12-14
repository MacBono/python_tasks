#!/usr/bin/python3
#				"Matrix multiplication"
import random
import numpy as np
matrix1=np.random.randint(10, size=(8,8))
matrix2=np.random.randint(10, size=(8,8))
matrix_prod=np.zeros((8,8), dtype=int)
for i in range(8):
	for j in range(8):
		for k in range(8):
			matrix_prod[i,j] += matrix1[i,k]*matrix2[k,j]

matrix_check = np.matmul(matrix1,matrix2)
print('Check : ')
for i in range(8):
	for j in range(8):
		if matrix_check[i,j]!=matrix_prod[i,j]:
			print('Improper multiplication!')
			break
print('Proper multiplication!')
print(matrix_prod)
print(matrix_check)



