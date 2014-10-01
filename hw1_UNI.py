__author__ = "Ramzi Abdoch"
__email__ = "raa2148@columbia.edu"

from path_node import PathNode
from UserString import MutableString
import sys

import argparse
parser = argparse.ArgumentParser(description='Robot Path Planning | HW 1 | COMS 4701')
parser.add_argument('-bfs', action="store_true", default=False , help="Run BFS on the map")
parser.add_argument('-dfs', action="store_true", default=False, help= "Run DFS on the map")
parser.add_argument('-astar', action="store_true", default=False, help="Run A* on the map")
parser.add_argument('-all', action="store_true", default=False, help="Run all the 3 algorithms")
parser.add_argument('-m', action="store", help="Map filename")

results = parser.parse_args()

# Explored/Frontier History dict, global
explored = {}
frontier_history = {}

if results.m=="" or not(results.all or results.astar or results.bfs or results.dfs):
	print "Check the parameters : >> python hw1_UNI.py -h"
	exit()

if results.all:
	results.bfs = results.dfs = results.astar = True

# Check dict if node has been explored
def hasBeenExplored(state):
	key = str(state[0]) + "," + str(state[1])
	if explored.get(key) != None:
		return True
	else:
		return False

# Check dict if node has been in the frontier
def hasBeenInFH(state):
	key = str(state[0]) + "," + str(state[1])
	if frontier_history.get(key) != None:
		return True
	else:
		return False

def isValidState(state):
	# Check if the state is within the map
	if state[0] > -1 and state[0] < width and state[1] > -1 and state[1] < height:
		# If the state is not an obstacle
		if arena[state[0]][state[1]] != "o":
			# If the state has not been explored
			if not(hasBeenExplored(state)):
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def addToExplored(state):
	key = str(state[0]) + "," + str(state[1])
	if (explored.get(key) != None):
		explored[key] = explored.get(key) + 1
	else:
		explored[key] = 1

def addToFH(state):
	key = str(state[0]) + "," + str(state[1])
	if (frontier_history.get(key) != None):
		frontier_history[key] = frontier_history.get(key) + 1
	else:
		frontier_history[key] = 1

def findInitialState(arena):
	# Iterate over rows of the map until "s" appears and return that state
	for i in range(0,width-1):
        	for j in range(0,height-1):
        		if isValidState([i,j]):
	        		if arena[i][j] == "s":
	        			print "Start state @ i: %d, j: %d" % (i, j)
	        			startState = [i,j]
	        			return startState

def isGoal(state):
	if arena[state[0]][state[1]] == "g":
		return True

def possibleActions(node):
	# Testing possible moves from state
	actions = []
	state = node.state
	cost = node.path_cost + 1

	up = [0,-1]
	left = [-1,0]
	down = [0,1]
	right = [1,0]

	# Try UP
	test_state = map(sum, zip(state,up))

	if isValidState(test_state):
		test_state.append("UP")
		test_state.append(cost)
		actions.append(test_state)

	# Try RIGHT
	test_state = map(sum, zip(state,right))

	if isValidState(test_state):
		test_state.append("RIGHT")
		test_state.append(cost)
		actions.append(test_state)

	# Try DOWN
	test_state = map(sum, zip(state,down))

	if isValidState(test_state):
		test_state.append("DOWN")
		test_state.append(cost)
		actions.append(test_state)

	# Try LEFT
	test_state = map(sum, zip(state,left))

	if isValidState(test_state):
		test_state.append("LEFT")
		test_state.append(cost)
		actions.append(test_state)

	return actions

def printPath(node, arena):

	path = []

	while node.path_cost > 0:
		path.append(node.state)
		node = node.parent

	print "Solution:"

	print path

	for i in range(0,width-1):
		for j in range(0,height-1):
			if arena[i][j] == "g":
				sys.stdout.write("g")
			elif [i,j] in path:
				sys.stdout.write("*")
			else:
				sys.stdout.write(arena[i][j])
		sys.stdout.write("\n")

def success(node, explored):
	# Output Map w/ Path
	print "Success, in %d moves!" % node.path_cost
	printPath(node, arena)
	exit()

def failure():
	# Output Sadface
	print "Failure. :("
	exit()

def bfs(arena):
	# BFS algorithm
	root_state = findInitialState(arena)
	node = PathNode(root_state, None, None, 0)

	if isGoal(node.state):
		success(node, [])

	# Instantiate FIFO Queue Frontier
	frontier = []

	# Add starting node
	frontier.append(node)
	addToFH(node.state)

	# Do While Loop
	while True:
		if len(frontier) < 1:
			print "Empty Frontier"
			failure()

		# Pop the first element from the queue
		node = frontier.pop(0)
		addToExplored(node.state)

		# Iterate over possible actions
		for action in possibleActions(node):
			# Create child node from action[x,y,action,cost]
			child = PathNode([action[0],action[1]], node, action[2], action[3])

			if not(hasBeenInFH(child.state) or hasBeenExplored(child.state) == True):
				if isGoal(child.state):
					success(child, explored)
				else:
					frontier.append(child)
					addToFH(child.state)

def dfs(arena):
	pass

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
	bfs(arena)
	print "BFS algorithm called"  # comment out later

if results.dfs:
	dfs(arena)
	print "DFS algorithm called"  # comment out later

if results.astar:
	# Call / write your A* algorithm
	print "A* algorithm called"  # comment out later
