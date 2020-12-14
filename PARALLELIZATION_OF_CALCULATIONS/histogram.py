#!/usr/bin/python3
import matplotlib.pyplot as plt
from multiprocessing.pool import Pool

def calcNum(n):
  print("Calcs Started on ", n)
  m = 3
  for i in range(100):
    m+=n
    m*=m
    m/=(n*m-n)
  return m

p= Pool(processes=3)
x = []
for i in range(30):
	x.append(i+1)
print(x)
result = p.map(calcNum, x)
p.close
p.join

print(result)
beans = []
for i in range(15):
	beans.append((i+1)/10)
plt.hist(result)
plt.show()