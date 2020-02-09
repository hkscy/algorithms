# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
#
# Given NxN grid of unit cells, must reach the southeast cell
# You have only two types of moves available:
# - a unit move to the east
# - a unit move to the south
# You can move into any cell, but you may not make a move 
# that would cause you to leave the grid. 
#
# Your rival, Labyrinth Lydia, has already solved the maze 
# before you, using the same rules described above! 
#
# Find a path such that you do not use any edge that Lydia 
# has used in her path. 

import random

DEBUG = False

def newRoute(opponent_path):
	# First attempt at solution - just take the opposite moves
	return ''.join(['E' if move=='S' else 'S' for move in opponent_path])

def main():
	# First line of input gives the number of test cases T
	testSetSize = int(input())

	for testNr in range(1, testSetSize+1):
		# each case consists of two lines.
		# The first line contains one integer N, giving the dimensions of the maze
		dimensions = int(input())
		
		# The second line contains a string P of 2N - 2 characters, each of which is 
		# either uppercase E (for east) or uppercase S (for south), representing 
		# Lydia's valid path through the maze. 
		opponent_path = input()
		
		# output one line containing Case #x: y
		# where y is a string of 2N - 2 characters each of which in {ES}
		path = newRoute(opponent_path)
		print("Case #{}: {}".format(testNr, path))

if __name__ == "__main__":
	main()
