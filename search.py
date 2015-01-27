from treelib import Tree
from Queue import Queue
from state import State

#given a init_state string s
#find the given goal state for the game
# the goal state is a state such that the string 
# as blacks on the left side and whites on the right
# with an x seperating the 2
def get_goal_state(s):
	'''returns the goal state of board of s'''
	length = len(s)
	blacks = ["b" for i in xrange(length//2)]
	whites = ["w" for i in xrange(length//2)]
	return "".join(blacks) + "x" + "".join(whites)

class Search:
	def __init__ (self, init_str, arg, cost):
		self.cost = cost
		self.tree = Tree()
		init_state = State(init_str)
		self.goal_state = State(get_goal_state(init_str))
		#data structure for Depth first search is a list (python list can be a stack)
		if arg == "DFS":
			self.L = [init_state]
		#data structure for Breadth first is a Queue import Queue class for L
		elif arg == "BFS":
			self.L = Queue()
			self.L.put(init_state)

		self.visited = [init_state] #list of visisted states
		self.tree.create_node(init_state.string, init_state.string) #root of search tree
		#need IDS, A*, greedy
	
	def uninformed_get(self):
		if isinstance(self.L, Queue):
			return self.L.get()
		elif isinstance(self.L, list):
			return self.L.pop()
	
	def uninformed_put(self,state):
		if isinstance(self.L, Queue):
			self.L.put(state)
		elif isinstance(self.L, list):
			self.L.append(state)
	
	def is_empty(self):
		if isinstance(self.L, Queue):
			return self.L.empty()
		elif isinstance(self.L, list):
			return not bool(self.L) #bool ([]) returns false 

	def uninformed_search(self):
		while not self.is_empty():
			node = self.uninformed_get()
			
			if not self.is_in_visited(node) : #don't expand node already expande donce
				self.visited.append(node)
			
			if self.check_for_goal():
				return self.path_to_goal()
			
			else:
				for i in range(len(node.string)):
					state = State(cpy=node) #reate a temp state parent
					if i != node.string.index('x'):
						state.move(i)
						if not self.is_in_visited(state):
							self.visited.append(state)
							self.uninformed_put(state)
							self.tree.create_node(state.string,state.string,parent=node.string)


	def is_in_visited (self,state):
		for s in self.visited:
			if s.string == state.string:
				return True
		return False

	def check_for_goal (self):
		'''returns True if goal_state is in visited'''
		for state in self.visited:
			if self.goal_state.string == state.string:
				return True
		return False


	def path_to_goal (self):
		node = self.tree[self.goal_state.string]
		move_list  = [node]

		while not node.is_root():
			node = self.tree[node.bpointer]
			move_list.append(node)
		

		#reverse move_list and print 
		for i,n in enumerate(reversed(move_list)):
			print n.tag, "step %d" %i, "move %d"%n.tag.index("x")
