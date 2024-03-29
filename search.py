import sys
sys.path.append("treelib/treelib/") #use static treelib if not in default packages
from tree import Tree
from Queue import Queue
from state import State


#Search contain all the methods and members to run the different searches
# self.tree is the search tree created by searches
# arg will be the search that is going to be performed (A-STAR, BFS, ... )
# init_str is the initial string will act as the root of the tree and the start of the search
# expanded will be a list of expanded nodes to reinsure a node is only expanded once
# cur_tree_id will be the id of a node in the tree each node must have a unique id
# cost_flag is True if using a variable cost or False if using a constant cost


class Search:
	def __init__ (self, init_str, arg, cost_flag):
		self.cost_flag = cost_flag
		self.tree = Tree()
		self.arg = arg
		init_state = State(0,0,init_str) 

		self.length = len(init_str) #length of puzzle used for making moves
		
		#data structure for BFS is a Queue import Queue class for L
		if arg == "BFS":
			self.L = Queue()
			self.L.put(init_state)
		
		else:
			if arg not in ["DFS","UCS","A-STAR","GS"]:
				arg = "DFS" #if not a valid search default to DFS
				
			self.L = [init_state] #only BFS uses Queue every other search will use a list
		

		self.expanded = [] #list of expanded states
		self.cur_tree_id = 1 #unique tree id per state added to the tree
		self.tree.create_node(init_state.string,init_state.tid) #creates the root node of the search tree

	# returns the needed node from structure L
	# in GS,UCS,A-STAR it requires a min heap.
	# use a list but sort the list by the given f-costs
	# UCS : "cost to of a path(number of moves)"
	# A-STAR : "path cost + number of tiles misplaced"
	# GS : "number of tiles misplaced"
	# since list does not have a remove from front
	# reverse the sorted list and pop.
	def get(self):
		if isinstance(self.L, Queue):
			state = self.L.get()
		
		elif isinstance(self.L, list):
			if self.arg == "UCS":
				self.L.sort(key = lambda n: (n.cost, n.tid), reverse=True) 

			elif self.arg == "A-STAR":
				self.L.sort(key = lambda n: ((n.cost + n.num_misplaced),n.tid), reverse=True)

			#returns lowest f cost where f(n)=h(n)
			elif self.arg == "GS":
				self.L.sort(key = lambda n: (n.num_misplaced,n.tid), reverse=True)

			state = self.L.pop()
			return state

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
	
	# generic search will handle all searches
	# the node to chosen for the search will depend on the get method 
	def search(self):
		while not self.is_empty():
			node = self.get()			
			if self.is_goal(node):
				break
			else:
				self.expand(node)

		self.path_to_goal(node)
	
	def expand(self,state):
		if not self.is_in_expanded(state):
			self.expanded.append(state) #
			for i in range(self.length):
				
				if self.cost_flag: #cost will be the steps for x 

					cost = abs(state.string.index("x") - i)  
					
				else:
					cost = state.cost + 1 #total path cost
				
				successor = State(self.cur_tree_id,cost, state.string) #create a copy of node to apply move then add to L and tree
				self.cur_tree_id += 1
				if i != state.string.index('x'): #don't move x into itself
					successor.move(i)
					self.put(successor) #put state into data structure L 
					self.add_to_tree(successor,state)
				


	def is_in_expanded (self, state):
		# checks expanded if a state as already been exanded
		return state in self.expanded

	def is_goal (self, state):
		# returns true if state as no misplaced tiles
		return not bool(state.num_misplaced) 

	def add_to_tree (self, state, parent):
		self.tree.create_node(state.string, state.tid, parent=parent.tid)

	def path_to_goal (self, goal):
		node = self.tree[goal.tid] 
		move_list  = [node]
		
		while not node.is_root():
			node = self.tree[node.bpointer]
			move_list.append(node)
		
		#reverse move_list because first node is the goal and you want first node to be root Path(root->goal)
		move_list = list(reversed(move_list))
		print "board movements start at the left index 0 "
		print "example initial wxb step 1: move 0 xwb"  
		print "step 0: ", move_list[0].tag
		for i in range(1, len(move_list)):
			print "step %i: " % i, "move %i"% move_list[i].tag.index("x"), move_list[i].tag

