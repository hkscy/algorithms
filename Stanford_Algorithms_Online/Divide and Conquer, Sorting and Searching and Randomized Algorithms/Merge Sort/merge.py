# Chris Hicks 2020
# Implementation of merge sort as discussed in Stanford Algorithms Course

import sys
import copy

# Merges two subarrays l, r
def merge(l, r, sortedList):
	n = len(l)+len(r)
	i = 0
	j = 0
	
	for k in range(0, n):

		if i < len(l) and j < len(r):
			if l[i] < r[j]:
				sortedList[k] = l[i]
				i += 1
			else:
				sortedList[k] = r[j]
				j += 1
				
		elif i>= len(l): # Copy remaining elements in r
			sortedList[k] = r[j]
			j += 1
			
		elif j>= len(r): # Copy remaining elements in l
			sortedList[k] = l[i]
			i+=1

def mergeSort(unsortedList):
	# Base-case for recursion (0 or 1 elements)
	if len(unsortedList) <= 1:
		return unsortedList
		
	# Split the input into two halves
	lSize = len(unsortedList)//2
	lHalf = copy.deepcopy(unsortedList[:lSize])
	rHalf = copy.deepcopy(unsortedList[lSize:])
	
	mergeSort(lHalf)
	mergeSort(rHalf)
	merge(lHalf, rHalf, unsortedList)

# Takes a list of integers to sort as argv input (space separated)
def main():
	
	try:
		unsortedList = [int(v.lstrip()) for v in sys.argv[1:]]
		
	except:
		print("Unexpected value(s) in input.")
		print("Please specify space-separated list of integers as input")
		sys.exit(-1)
		
	mergeSort(unsortedList)
	print(unsortedList)
	
if __name__ == "__main__":
	main()
