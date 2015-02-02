from search import Search 
import sys

#parse input from command line
#will return a tuple of search alg, init_str, and cost


#take in a string that could be the intial board 
#return True if its valid else return False
def is_valid_start(s):
	#board must be odd numbers and less then 13
	if len(s) % 2 == 0 or (0 < len(s) > 13):
		return False
	#count of b and w must be the same and only 1 x must occur
	return (s.count("w") == s.count("b") and s.count("x") == 1)

def is_valid_search(s):
	return s in ["UCS","GS", "BFS","A-STAR","DFS"]


if __name__ == "__main__":
	
	#main input to run the program will be python main.py <starting positions> <BFS|A-STAR|UCS|DFS|GS> [-cost] 
	#if cost is passed then use variable cost else use constant cost for search

	init_str = sys.argv[1].lower()   # change input
	search_alg = sys.argv[2].upper() # avoid case issues
	
	while not is_valid_start(init_str):
		print "Please enter a valid starting board"
		init_str = raw_input("starting board: ").lower()
	
	while not is_valid_search(search_alg):
		print "Please enter a valid search algorithm"
		search_alg = raw_input("enter a valid search (UCS,GS,BFS,A-STAR,DFS): ").upper()
	
	try:
		cost_flag = bool(sys.argv[3]) #if cost exists cost_flag will be true

	except IndexError:
		cost_flag = False 

	finally:
		s = Search(init_str, search_alg, cost_flag)
		s.search()

