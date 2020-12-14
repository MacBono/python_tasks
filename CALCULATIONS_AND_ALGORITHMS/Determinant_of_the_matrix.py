#!/usr/bin/python3
#				"Determinant of the matrix"
import random
import numpy as np
m_size=int(input('Matrix size: '))
val_range=input('Values upper limit: ')
matrix=np.random.randint(val_range, size=(m_size,m_size))

det = np.linalg.det(matrix)
print(matrix)
print(det)



