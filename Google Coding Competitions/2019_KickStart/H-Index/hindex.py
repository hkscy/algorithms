# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a274e
#
# Jorge has written N papers in his lifetime. The i-th paper has Ai citations. 
# The number of citations that each paper has will never change after it is written. 
# Please help Jorge determine his H-index score after each paper he wrote. 
#
# "The h-index is defined as the maximum value of h such that the given author/journal
# has published h papers that have each been cited at least h times."
#
# limits: H-index therefore will always be less than or equal to (leq) the max number of citations 
# any single paper has, and also leq the total number of papers. Will be greater than or equal to 0.
from queue import PriorityQueue

# Brute force h-index. 
# This is expensive but functional ~ n comparisons for each of n subproblems. O(n^2)
def brute_force_hindex(A):
	h_list = []
	for citations_list in [A[:i] for i in range(1, len(A)+1)]:
		# Lets find some limits first
		lower_limit = min(len(citations_list), min(citations_list))
		upper_limit = len(citations_list)
		h_index = lower_limit
		for h in range(lower_limit, upper_limit+1):
			count_h = 0
			# For each candidate h-index, check whether it is satisfied by counting 
			for n_citations in citations_list:
				if h <= n_citations:
					count_h += 1
			if count_h >= h: # Update h-index if satisfied
				h_index = h
			else:
				break
		h_list.append(str(h_index))
	return ' '.join(h_list)

# Lets try to reuse our hard work rather than computing h from scratch for each sub-list
# of citation counts. Note that the h-index can only ever go up as definedf for this problem.
# Using a priority queue (ordered heap) allows O(log n) operations so O(nlogn) overall.
def additive_h_index(citations_list):
	lower_limit = min(len(citations_list), min(citations_list))
	upper_limit = len(citations_list)
	h_queue = PriorityQueue()
	h_index = 0
	h_list = []
	for citation_count in citations_list:
		# If the current citation_count is bigger than the current h_index, add it in the priority queue
		if citation_count > h_index:
			h_queue.put(citation_count)
		# Remove all the citation counts from the priority queue which is not greater than the current h_index
		least = h_queue.get()
		while(least <= h_index):
			least = h_queue.get()
		h_queue.put(least)
		# If the size of priority queue is not less than the current answer + 1, increment the answer by 1
		if h_queue.qsize() >= h_index+1:
			h_index += 1
		h_list.append(str(h_index))
	return ' '.join(h_list)

def main():
	# First line of input gives the number of test cases T
	testSetSize = int(input())

	for testNr in range(1, testSetSize+1):
		#Each test case begins with a line containing N, the number of papers Jorge wrote.
		N = int(input())
		
		# The second line contains N integers. The i-th integer is A_i, the number of citations the i-th paper has. 
		A = [int(A_i) for A_i in input().split(' ')]
		
		# Output one line containing Case #x: y, where y is a space-separated list of integers.
		# The i-th integer is the H-index score after Jorge wrote his i-th paper. 
		h_index = additive_h_index(A)
		print("Case #{}: {}".format(testNr, h_index))

if __name__ == "__main__":
	main()
