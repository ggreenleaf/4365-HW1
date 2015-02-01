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




if __name__ == "__main__":
	init_str = sys.argv[1].lower()
	search_alg = sys.argv[2].upper()
	cost = sys.argv[3]
	if is_valid_start(init_str):
		s = Search(init_str, search_alg, cost)
		s.search()
	else:
		print "invalid board"
