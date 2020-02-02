# Chris Hicks 2020
# 
# Give an algorithm that identifies the second-largest number in an 
# array (of distinct elements!), using at most n+log⁡_2(n)−2 comparisons.
#
# Reads the array of integers from the input file where the first line 
# of file specifies the array size. We assume no duplicates and that
# the size of the array is a power of 2.
# 
# Credit to https://cs.stackexchange.com/questions/83022/find-largest-and-second-largest-elements-of-the-array
# For discussion of optimal method
import copy

# Brute force method would be to loop through the array keeping a tuple
# of largest and second largest element in memory. Two comparisons 
# would be made for every element in the array so *2n total*. O(n)
# - Can just compare largest and move other element down if greater?
# - NO, this doesn't work if the second largest comes after the first.
def bruteForce_PenultimateMax(array):
		if len(array)<2:
			return None
		elif len(array) == 2:
			return min(array[:2]) # 1 comparison
		else:
			a, b = 0, 0
			for value in array:
				if value > a:
					b = a
					a = value
				elif value > b:
					b = value
			return b

# Lets try to do better than brute force (again)!
# We can consider the array pairwise as (first, second) and "construct an array"
# of size n/2 which contains only the pairwise firsts. 
# The second biggest element will either be in this list or it will be
# the second element from the pair that contained the biggest element in first.
#
# Overall this algorithm does n/2 + n + 1 comparisons. Approx 1.5n.
# Still not better than n+log⁡_2(n)−2 yet! 
def tournament_PenultimateMax(array):
	A = copy.deepcopy(array)
	
	for idx in range(0, len(array), 2):	# Compare the elements pairwise - n/2 comparisons
		if A[idx] < A[idx+1]: 			# Swap if necessary, so that pair indexing is known
			small = A[idx]
			A[idx] = A[idx+1]
			A[idx+1] = small
	
	# Now we know that the second biggest element is either in first
	# or it is in the pair that first came from
	# Using the brute force approach we can find these values in n comparisons
	first, first_idx, second = 0,0,0
	
	for idx in range(0, len(array), 2):
		if A[idx] > first:
			second = first
			first = A[idx]
			first_idx = idx
		elif A[idx] > second:
			second = A[idx]
	
	# Finally check if the second largest value is second or the pair of first
	if second > A[first_idx+1]: # 1 comparison
		return second
	else:
		return A[first_idx+1]
		
# Using recursion and ideas from tournament_PenultimateMax to achieve n+log⁡_2(n)−2
# Returns indices in the array rather than the element values, because we need to
# keep track of the pairwise value tuples.
def tournament_recursive_PenultimateMax(array):
	A = copy.deepcopy(array)
	
	# Base-case for recursion
	if len(A) == 2:
		if A[0] > A[1]:	# 1 comparison
			return (0, 1)
		else:
			return (1, 0)
	
	# Keep track of the biggest elements in A and also whether a swap was performed.
	biggest = [0]*(len(A)//2)
	swap_offset = [0]*(len(A)//2)
	
	for idx in range(0, len(array)//2):	# n comparisons
		if A[2*idx] < A[2*idx+1]:
			small = A[2*idx]
			A[2*idx] = A[2*idx+1]
			A[2*idx + 1] = small
			swap_offset[idx] = 1	# If we have swapped then the offset is 1
		biggest[idx] = A[2*idx]
		
	# Recurse onto the set of biggest elements
	(big_idx, small_idx) = tournament_recursive_PenultimateMax(biggest)
	
	# Map back from biggest to array (keep track of pair indices)
	big_offset = swap_offset[big_idx]
	small_offset = swap_offset[small_idx]
	big_idx *= 2
	small_idx *= 2
	
	if A[big_idx+1] > A[small_idx]: # Check if pair of biggest element is second largest
		small_idx = big_idx+1
		small_offset = 0 - big_offset
	
	return (big_idx + big_offset, small_idx + small_offset)

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
		
	print("Read {} array elements".format(arraySize))
	
	secondBiggestInt = bruteForce_PenultimateMax(A)

	assert(tournament_PenultimateMax(A) == secondBiggestInt)
	assert(A[tournament_recursive_PenultimateMax(A)[1]] == secondBiggestInt)
	
	print("{} is the second biggest element!".format(secondBiggestInt))
	
if __name__ == "__main__":
	main()
