from treelib import Tree
from Queue import Queue
from state import State
from math import factorial
#given a init_state string s
#find the given goal state for the game
# the goal state is a state such that the string 
# as blacks on the left side and whites on the right
# with an x seperating the 2
def get_goal_string(s):
	'''returns the goal state of board of s'''
	length = len(s)
	blacks = ["b" for i in xrange(length//2)]
	whites = ["w" for i in xrange(length//2)]
	return "".join(blacks) + "x" + "".join(whites)


class Search:
	def __init__ (self, init_str, arg, cost):
		self.cost = cost
		self.tree = Tree()
		self.arg = arg
		init_state = State(0,0,s=init_str) #tid used for tree 

		length = len(init_str)
		
		#if goal state is the last state visited then it will be this state number
		max_num_states = factorial(length) / (factorial(length//2)**2)
		self.goal_state = State(max_num_states,0, s=get_goal_string(init_str))
		

		#data structure for BFS is a Queue import Queue class for L
		if arg == "BFS":
			self.L = Queue()
			self.L.put(init_state)
		else:
			if arg not in ["DFS","UCS","A-STAR","GS"]:
				arg = "DFS" #if not a valid search default to DFS
	
			self.L = [init_state] #only BFS uses Queue every other search will use a list
		

		self.visited = [] #list of visisted states
		self.cur_tree_id = 1
		self.tree.create_node(init_state.string,init_state.tid)


	def get(self):
		if isinstance(self.L, Queue):
			return self.L.get()
		elif isinstance(self.L, list):
			if self.arg == "UCS":
				self.L.sort(key=test_sort, reverse=True) 
				return self.L.pop()
			if self.arg == "A-STAR":
				self.L.sort(key=lambda n: n.cost + n.num_misplaced, reverse=True)
				return self.L.pop()
			if self.arg == "GS":
				self.L.sort(key=lambda n: n.num_misplaced, reverse=True)
				return self.L.pop()
			else:	
				return self.L.pop()

	
	def put(self,state):
		if isinstance(self.L, Queue):
			self.L.put(state)
		elif isinstance(self.L, list):
			self.L.append(state)
	
	def is_empty(self):
		if isinstance(self.L, Queue):
			return self.L.empty()
		elif isinstance(self.L, list):
			return not bool(self.L) #bool ([]) returns false 

	def search(self):
		while not self.is_empty():
			node = self.get()			
			if self.check_for_goal(node):
				return self.path_to_goal(node)
			else:
				self.expand(node)

	def expand(self,node):
		if not self.is_in_visited(node):
			self.visited.append(node) #
			for i in range(5):
				cost = node.cost + 1 #total path cost
				state = State(self.cur_tree_id,cost, cpy=node) #create a copy of node to apply move then add to L and tree
				self.cur_tree_id += 1
				if i != node.string.index('x'): #don't move x into itself
					state.move(i)
					self.put(state) #put state into data structure L 
					self.add_to_tree(state,node)


	def is_in_visited (self, state):
		'''checks visited if a state as already been exanded'''
		return state.string in [s for s in self.visited]

	def check_for_goal (self, node):
		'''returns True if node has 0 misplaced tiles'''
		return not bool(node.num_misplaced) #goal state reached if misplaced tiles is 0

	def add_to_tree (self, node, parent):
		self.tree.create_node(node.string, node.tid, parent=parent.tid)

	def path_to_goal (self, goal):
		#the goal state will be the last node added to the tree -> cur_tree_id - 1
		node = self.tree[goal.tid] 
		move_list  = [node]
		while not node.is_root():
			node = self.tree[node.bpointer]
			move_list.append(node)
		
		#reverse move_list and print 
		for i,n in enumerate(reversed(move_list)):
			print n.tag, "step %d" %i, "move %d"%n.tag.index("x")
