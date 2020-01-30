# Given N, find A+B=N such that neither A|B includes the digit 4
#
# The first line of the input gives the number of test cases, 
# T. T test cases follow; each consists of one line with an 
# integer N. 
#
# 1 ≤ T ≤ 100
# AT LEAST one of the digits is 4
# 10 secs per test set
# memory limit 1gb
import random

DEBUG = False

# Returns true if string t contains the digit 4
def contains4(t):
	return '4' in str(t)

# Given 1 ≤ T ≤ 100, find A+B=N such that 
# neither A|B includes the digit 4
def solve_random(t):
	# Pick a random a, compute b and check no 4's
	while(True):
		a = random.randint(1,t-1)
		if '4' not in str(a):
			b = t-a
			if '4' not in str(b):
				return a,b
				
# Given 1 ≤ T ≤ 100, find A+B=N such that 
# neither A|B includes the digit 4
def solve_constructive(t):
	# Replace each 4 in t with 2 and write B correspondingly
	a = ''.join(['2' if tval == '4' else tval for tval in str(t)])
	b = ''.join(['2' if tval == '4' else '0' for tval in str(t)])
	return a,b

def main():
	# First line of input gives the number of test cases T
	testSetSize = int(input())

	for testNr in range(1, testSetSize+1):
		testValue = int(input())
		a,b = solve_constructive(testValue)
		# For each test case, output one line containing Case #x: A B
		print("Case #{}: {} {}".format(testNr, a, b))


if __name__ == "__main__":
	main()
