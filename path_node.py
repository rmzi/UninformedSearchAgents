class Path_Node:
	state, parent, action, path_cost = [0,0], None, None, 0

	def __init__(self, state, parent, action, cost):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = action

	def __init__(self, state, cost):
		self.state = state
		self.cost = cost