# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

# Pangrams are phrases that use each letter of the English alphabet at least once
# We devised an encryption scheme based on factoring products of two large prime numbers
#
# - We chose 26 different prime numbers, none of which is larger than some integer N.
# - We sorted those primes in increasing order. Then, we assigned the smallest prime 
#   to the letter A, the second smallest prime to the letter B, and so on.
# - Everyone on the team memorized this list.
#
# Now, whenever we want to send a pangram as a message, we first remove all spacing to 
# form a plaintext message. Then we write down the product of the prime for the first 
# letter of the plaintext and the prime for the second letter of the plaintext. 
# Then we write down the product of the primes for the second and third plaintext letters, 
# and so on, ending with the product of the primes for the next-to-last and last plaintext 
# letters. This new list of values is our ciphertext. The number of values is one smaller 
# than the number of characters in the plaintext message. 
#
# For example, suppose that N = 103 and we chose to use the first 26 odd prime numbers, 
# because we worry that it is too easy to factor even numbers. Then A = 3, B = 5, C = 7, D = 11, 
# and so on, up to Z = 103. Also suppose that we want to encrypt the CJ QUIZ... pangram above, 
# so our plaintext is CJQUIZKNOWBEVYOFDPFLUXALGORITHMS. Then the first value in our ciphertext 
# is 7 (the prime for C) times 31 (the prime for J) = 217; the next value is 1891, and so on, 
# ending with 3053. 
# A = 3, B = 5, C = 7, D = 11, E = 13, F = 17, G = 19, H = 23, I = 29, J = 31, K = 37, L = 41
# M = 43, N = 47, O = 53, P = 59, Q = 61, R = 67, S = 71, T = 73, U = 79 ,V =83  W = 89, 
# X = 97, Y =101 , Z =103
#
# We will give you a ciphertext message and the value of N that we used. 
# We will not tell you which primes we used, or how to decrypt the ciphertext. 
# Do you think you can recover the plaintext anyway? 
#
# 1 ≤ T ≤ 100.
# Time limit: 20 seconds per test set.
# Memory limit: 1 GB.
# 25 ≤ L ≤ 100.
# The plaintext contains each English alphabet letter *at least* once. 

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# We can't efficiently factor large primes but we can efficiently find the GCD of two primes
# The gcd of two numbers also divides their difference
def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a % b)

def solve_using_Euclid(n, l, ciphertext_list):
	ciphertext_list = [int(c) for c in ciphertext_list]
	l = int(l)+1
	factored_ct = [0]*l
	# Find two adjacent elements with a GCD > 1
	for c_idx in range(1,l):
		factor_1 = gcd(ciphertext_list[c_idx-1], ciphertext_list[c_idx])
		if(factor_1 > 1):
			#Found first factor!
			factored_ct[c_idx] = factor_1
			break
	
	# Run forwards from c_idx factoring the remainder of the message
	for fwd_c_idx in range(c_idx+1, l):
		factored_ct[fwd_c_idx] = ciphertext_list[fwd_c_idx-1]//factored_ct[fwd_c_idx-1]
		
	# Run backwards from c_idx factoring the remainder of the message
	for bk_c_idx in range(c_idx-1, -1, -1):
		factored_ct[bk_c_idx] = ciphertext_list[bk_c_idx]//factored_ct[bk_c_idx+1]
		
	# Remove duplicates when creating cipher
	cipher = dict(zip(sorted(set(factored_ct)), alphabet))
	#print(factored_ct)
	#print(cipher)
	return "".join([cipher.get(c) for c in factored_ct])

	
def main():
	# First line of input gives the number of test cases T
	testSetSize = int(input())

	for testNr in range(1, testSetSize+1):
		# Each case consists of two lines.
		# The first line contains two integers: N, as described above, and L, 
		# the length of the list of values in the ciphertext. 
		n,l = input().split(" ")
		
		# The second line contains L integers: the list of values in the ciphertext. 
		ciphertext_list = input().split(" ")
		
		# output one line containing Case #x: y
		msg = solve_using_Euclid(n, l, ciphertext_list)
		print("Case #{}: {}".format(testNr, msg))

if __name__ == "__main__":
	main()

