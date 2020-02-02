# Chris Hicks 2020
# Implementation of "count split inversions" using the recursive merge-sort method.
#
# Reads an array of integers from an input file and counts the split inversions.
# First line of file specifies the array size.

import sys
import copy

# Merges two subarrays l, r - counts the number of split inversions while merging.
def merge_and_countSplitInv(l, r, sortedList):
	n = len(l)+len(r)
	i = 0
	j = 0
	numSplitInv = 0
	
	for k in range(0, n):

		if i < len(l) and j < len(r):
			if l[i] < r[j]:
				sortedList[k] = l[i]
				i += 1
			else:
				sortedList[k] = r[j]
				j += 1
				# Increment number of split inversions by remaining elements in l[i]
				numSplitInv += (len(l)-i)
				
		elif i>= len(l): # Copy remaining elements in r
			sortedList[k] = r[j]
			j += 1
			
		elif j>= len(r): # Copy remaining elements in l
			sortedList[k] = l[i]
			i+=1
	
	return numSplitInv

def sort_and_count(unsortedList):
	# Base-case for recursion (0 or 1 elements)
	if len(unsortedList) <= 1:
		return 0
		
	# Split the input into two halves
	lSize = len(unsortedList)//2
	lHalf = copy.deepcopy(unsortedList[:lSize])
	rHalf = copy.deepcopy(unsortedList[lSize:])
	
	x = sort_and_count(lHalf)
	y = sort_and_count(rHalf)
	z = merge_and_countSplitInv(lHalf, rHalf, unsortedList)
	return x+y+z

# Reads the list of integers from input, first line specifies size.
def main():
	
	try:
		arraySize = int(input())
		A = [0]*arraySize
		for index in range(0, arraySize):
			A[index] = int(input())
		
	except:
		print("Unexpected value(s) in input.")
		print("Please specify one integer on each line of the file.")
		sys.exit(-1)
		
	numSplitInv = sort_and_count(A)
	print(A)
	print(numSplitInv)
	
if __name__ == "__main__":
	main()
