__author__ = "Ramzi Abdoch"
__email__ = "raa2148@columbia.edu"

import argparse
parser = argparse.ArgumentParser(description='Robot Path Planning | HW 1 | COMS 4701')
parser.add_argument('-bfs', action="store_true", default=False , help="Run BFS on the map")
parser.add_argument('-dfs', action="store_true", default=False, help= "Run DFS on the map")
parser.add_argument('-astar', action="store_true", default=False, help="Run A* on the map")
parser.add_argument('-all', action="store_true", default=False, help="Run all the 3 algorithms")
parser.add_argument('-m', action="store", help="Map filename")

results = parser.parse_args()

if results.m=="" or not(results.all or results.astar or results.bfs or results.dfs):
	print "Check the parameters : >> python hw1_UNI.py -h"
	exit()

if results.all:
	results.bfs = results.dfs = results.astar = True

def findInitialState(arena):
	# Iterate over rows of the map until "s" appears and return that state
	for j in range(0,height):
        	for i in range(0,width):
        		if arena[j][i] == "s":
        			print "Start state @ i: %d, j: %d" % (i, j)
        			startState = [i,j]
        			return startState
        			
def isValidState(state):
	# Check if the state is within the map
	print arena[state[0]][state[1]]
	if state[0] > -1 and state[0] < width and state[1] > -1 and state[1] < height:
		# If the state is not an obstacle, it's valid
		if arena[state[0]][state[1]] != "o":
			return True
		else:
			return False
	else:
		return False

def possibleActions(state):
	# Testing possible moves from state
	actions = []

	up = [0,-1]
	left = [-1,0]
	down = [0,1]
	right = [1,0]

	# Try UP
	test_state = map(sum, zip(state,up))
	print test_state

	if isValidState(test_state):
		actions.append(test_state)
		print actions

# Reading of map given and all other initializations
try:
    with open(results.m) as f:
        arena = f.read()
        arena = arena.split("\n")[:-1]
        width = len(arena)
        height = len(arena[0])

except:
	print "Error in reading the arena file."
	exit()
  
# Internal representation  
print arena 

print "The arena of size "+ str(len(arena)) + "x" + str(len(arena[0]))
print "\n".join(arena)

if results.bfs:
	# Call / write your BFS algorithm
	root = findInitialState(arena)
	possibleActions(root)
	print "BFS algorithm called"  # comment out later

if results.dfs:
	# Call / write your DFS algorithm
	print "DFS algorithm called"  # comment out later

if results.astar:
	# Call / write your A* algorithm
	print "A* algorithm called"  # comment out later

"""
class Path_Node:
	state, parent, action, path_cost = [0,0], None, None, 0

	def __init__(self, data):
		self
"""
