# Chris Hicks 2020
#
# An implementation of the randomised quicksort algorithm
# as discussed in Stanford Algorithms Course.
# Additionally counts the total number of comparisons made
# between elements in the input array.
#
# Input: A file of integers, one per line, first line specifies size.
# Output: Array sorted in increasing size and the number of comparisons
#         made by quicksort when sorting.

import numpy as np # Using numpy so that memory is shared between slices
				   # and their source

nComparisons = 0

# Choose the "random" array pivot as 0
def choosePivot_zero(array):
	return 0

# Choose the "random" array pivot as the median of the first, middle and last values
def choosePivot_median(array):
	# Choose median of three from first, median and last elements in array
	if len(array) <= 2:
		return 0
	if len(array) % 2 == 0:					# array size is even
		median_index = (len(array)//2) - 1
	else: 									# array size is odd
		median_index = len(array)//2
	
	choices = [array[0], array[median_index], array[len(array)-1]]
	choices.remove(max(choices))
	choices.remove(min(choices))
	return list(array).index(choices.pop())

# Partition the array about element l_idx such that the output comrprises
# a reshuffled array in which all elements left of l_idx are lesser than 
# and all elements right of l_idx are greater than.
def partition(array, l_idx, r_idx):
	global nComparisons
	pivot_value = array[l_idx]
	i = l_idx+1
	for j in range(l_idx+1, r_idx):
		nComparisons += 1
		if array[j] < pivot_value:
			# Swap array[j] with array[i]
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
			i += 1
	# Swap the pivot_value into it's final place
	array[l_idx] = array[i-1]
	array[i-1] = pivot_value
	
	return array[:i-1], array[i:]

def quicksort(array):
	if len(array) <= 1:
		return
	pivot_index = choosePivot_median(array)
	# We have to swap the pivot into the first position of the array
	array[0], array[pivot_index] = array[pivot_index], array[0]
	left, right = partition(array, 0, len(array))
	quicksort(left)
	quicksort(right)

def main():
	
	try:
		sizeOfArray = int(input())
		array = np.array([0]*sizeOfArray)
		for idx in range(sizeOfArray):
			array[idx] = int(input())
		
	except:
		print("Unexpected input. Expects file of integers,"
				"one per line, first line specifies size.")

	quicksort(array)
	print(array)
	print("QuickSort made {} total comparisons when sorting the array.".format(nComparisons))
	
if __name__ == "__main__":
	main()
