'''
Overview: This script will provide examples of algorithms that have loglinear time complexity. 
The purpose here is to build a strong mental model of what loglinear time looks like. This is 
my first focus since this is the one I understand the least. 
'''



def merge_sort(_list):
	'''
	1. Take a list as an input 
	2. Find the midpoint of that list 
	3. Separate the list into a left list and a right list 
	4. Loop from i to the length of the list
		- if left list index is greater than right list, add th

	'''
	if len(_list) < 2: ## base condition for recursion
		return 

	midpoint = int(len(_list)/2)

	left = _list[:midpoint]

	right = _list[midpoint:]

	merge_sort(left)
	merge_sort(right)


	i, j, k = 0,0,0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			_list[k] = left[i]
			i += 1
		else:
			_list[k] = right[j]
			j += 1
		k+= 1

	while i < len(left):
		_list[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		_list[k] = right[j]
		j += 1
		k += 1

	print(_list)


if __name__=='__main__':

	l = [3,5,2,6,3,7,4]
	merge_sort(l)
