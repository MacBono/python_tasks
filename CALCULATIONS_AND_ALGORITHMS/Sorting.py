#!/usr/bin/python3
#				"Sorting"
def sorting(list):
	flag = True
	while flag:
		flag = False
		for i in range(len(list)-1):
			if list[i] < list[i+1]:
				list[i], list[i+1] = list[i+1], list[i]
				flag = True

import random
numbers = []
for i in range(50):
	numbers.append(random.randint(0,100))
numbers_compare = numbers
sorting(numbers)
sorted(numbers_compare, reverse=True)
for i in range(len(numbers)-1):
	if numbers[i]!=numbers_compare[i]:
		print('Not sorted properly')
		break
print('List sorted properly!')
print('Lists manual check: ')
print(numbers)
print(numbers_compare)



