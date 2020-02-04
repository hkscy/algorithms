# Chris Hicks 2020
#
# Based on Microsoft Technical Interview question: 
# "Given a string, write an algorithm that will determine if it is a palindrome"
# Input: string of characters, Output: True (palindrome) False (palindrome)
# 
# What is a palindrome? 
# - A sequence of characters which reads the same backward as forward
# - Sentence-length palindromes may be written when allowances are made for 
# adjustments to capital letters, punctuation, and word dividers
#
# Some examples are "02022020":True , "Chris":False, , "Anna":True
# "Step on no pets":True, "Lobster Stew":False
#
# Can I use libraries? if so re for regular expressions could be used
# or  methods and variables from string library and e.g. string.punctuation
import string as strings
import timeit

examples = {"02022020":True , "Chris":False, "Anna":True, 
	"Step on no pets":True, "Lobster Stew":False,
	" ":True, "":True}

# In the permissive setting, return a string with no capitalisation or whitespace
def permissive(string):
	string = string.casefold() 			# n comparisons
	string = string.replace(" ", "")	# n comparisons
	return string

# Simply check whether all of the "opposite" characters in string have 
# the same value. Wasteful since we're duplicating our effort.
def basic_is_palindrome(string):
	return string == string[::-1]

# Can we do better? We can compare just n//2 elements
def fast_is_palindrome(string):
	# If string has odd length than ignore middle character
	n = len(string)
	if n%2 != 0:
		string = string[0:n//2]+string[n//2+1:]
	for idx in range(n//2):
		if string[idx] != string[-idx-1]:
			return False
	return True


def main():	
	for example in examples:
		# If we want to be disregard punctuation and whitespace
		example_clean = permissive(example)
		
		if basic_is_palindrome(example_clean) == examples.get(example):
			print("Basic method PASS for example \"{}\"".format(example))
		else:
			print("Basic method FAIL for example \"{}\"".format(example))
			
		if fast_is_palindrome(example_clean) == examples.get(example):
			print("Fast method PASS for example \"{}\"".format(example))
		else:
			print("Fast method FAIL for example \"{}\"".format(example))
		print()

if __name__ == "__main__":
	main()
