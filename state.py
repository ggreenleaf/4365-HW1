class State:
	def __init__(self, tid, s=None, cpy=None):
		#need to check for valid inputs
		if cpy:
			self.cpy_constructor(cpy)
		else:
			self.non_cpy_constructor(s)
		
		self.tid = tid
	
	def cpy_constructor(self, cpy):
		self.string = cpy.string

	def non_cpy_constructor(self,s):
		self.string = s.lower()

	def move(self, i):
		'''move index with index where 'x' occurs '''
		if 0 > i > len(self.string):
			print "invalid index"
			return
		
		x_indx = self.string.index('x')
		str_list = list(self.string)
		str_list[x_indx], str_list[i] = str_list[i], str_list[x_indx]
		
		self.string = "".join(str_list)


