# Chris Hicks 2020
#
# Selection of the ith order statistic (e.g. smallest or median) of an array is a
# fundamentally easier problem than sorting and can be done in linear time!
#
# Input: A file of integers, one per line, first line specifies size and i.
# Output: The ith order statistic of the input array of integers.
import random
import numpy as np

nComparisons = 0

# Partition the array about element p such that the output comrprises
# a reshuffled array in which all elements left of p are lesser than,
# and all elements right of p are greater than. 
# Returns the the final position of p in the array
def partition(array):
	global nComparisons
	n = len(array)
	# Choose a pivot index p_idx from array uniformly "at random"
	p_idx = random.randint(0, n-1)
	# Swap the pivot into the first position of the array
	array[0], array[p_idx] = array[p_idx], array[0]
	pivot_value = array[0]
	i = 1
	for j in range(1, len(array)):
		nComparisons += 1
		if array[j] < pivot_value:
			# Swap array[j] with array[i]
			array[j], array[i] = array[i], array[j]
			i += 1
	# Swap the pivot_value into it's final place
	array[0], array[i-1] = array[i-1], array[0]
	return (i-1)

# Linear time method for finding the ith order statistic of an input array
def rselect(array, i):
	n = len(array)
	if n == 1:
		return array[0]
	
	# Partition array around a random pivot and return the index of the new pivot
	p = partition(array)
	
	if p == i:		# Once p==i then we have found the ith order statistic
		return array[p]
	elif p > i:		# Recurse onto left side of array only
		return rselect(array[0:p], i)
	else:			# Recurse onto right side only, applying offset to i
		return rselect(array[p+1:], i - p - 1)

def main():
	try:
		arraysize, i = [int(val) for val in input().split(' ')]
	except:
		print("First line of input must specify array size and the ith order to be found.")
		quit(-1)
	
	array = np.array([0]*arraysize)
	try:
		for idx in range(arraysize):
			array[idx] = int(input())
	except:
		print("Only integers allowed in input, please check input file.")
		quit(-1)
	
	ith_statistic_value = rselect(array, i)
	print("The {}th order statistic is {}.".format(i, ith_statistic_value))

if __name__ == '__main__':
	main()
