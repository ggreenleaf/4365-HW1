class State:
	def __init__(self, tid, cost, s):
		#need to check for valid inputs

		self.string = s.lower()
		self.tid = tid
		self.cost = cost
		self.num_misplaced = self.count_misplaced()
	
	def __eq__(self, other):
		return self.string == other.string

	
	#our h(n) function
	#count the number of tiles out of place for example
	# the board wwxbb will have 4 tiles misplaced because
	def count_misplaced(self): 
		'''returns the number of outplaced tiles in string'''
		n = len(self.string)
		misplaced = 0
		for i in range(n):
			if i < n//2 and self.string[i] != "b":
				misplaced += 1
			if i == n//2 and self.string[i] != "x":
				misplaced += 1
			if i > n//2 and self.string[i] != "w":
				misplaced += 1
		
		return misplaced


	def move(self, i):
		'''move index with index where 'x' occurs '''
		if 0 > i > len(self.string):
			print "invalid index"
			return
		
		x_indx = self.string.index('x')
		str_list = list(self.string) #for easier swapping use create a list of chars
		str_list[x_indx], str_list[i] = str_list[i], str_list[x_indx]
		
		self.string = "".join(str_list) #join the list back into a string
		self.num_misplaced = self.count_misplaced() #after move re-count number misplaced 

