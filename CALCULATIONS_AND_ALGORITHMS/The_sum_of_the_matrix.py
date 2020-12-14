#!/usr/bin/python3
#				"The sum of the matrix"
import random
import numpy as np
matrix1=np.random.rand(128,128)
matrix2=np.random.rand(128,128)
matrix_sum=np.zeros((128,128))

for i in range(128):
	for j in range(128):
		matrix_sum[i,j] = matrix1[i,j]+matrix2[i,j]

print('Check (part of matrices): ')

print('First matrix: ')
print(matrix1[0:2,0:2])
print('Second matrix: ')
print(matrix2[0:2,0:2])
print('Sum: ')
print(matrix_sum[0:2,0:2])




