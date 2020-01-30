# Chris Hicks 2020
# Karatsuba multiplication for Stanford Algorithms course.
import sys
from math import ceil, floor

# Compute x*y using Karatsuba multiplication
def karatsuba(x, y):
	# Base case for recursion
	if len(str(x)) <= 1 and len(str(y)) <= 1:
		return int(x)*int(y)
	
	n = max(len(str(x)), len(str(y)))
	m = ceil(n/2)
	
	a = floor(int(x) / 10**m)
	b = int(x) % (10**m)
	c = floor(int(y) / 10**m)
	d = int(y) % (10**m)
	
	ac = karatsuba(a, c)
	bd = karatsuba(b, d)
	e = karatsuba(a+b, c+d) - ac - bd
	
	return int(ac*(10**(m*2)) + e*(10**m) + bd)

# Read two integers from argv, multiply them and print the result.
def main():
	if len(sys.argv) != 3:
		print("Provide two positive integers to be multiplied as arguments.")
	else:
		x = sys.argv[1]
		y = sys.argv[2]
		z = karatsuba(x, y)
		print(z)
		
if __name__ == "__main__":
	main()
