<h3>Group Members<h3>

<h3>List of Source Files</h3>
folder structure should like something like this after unzipping project
	
	.
	├── README.MD
	├── main.py
	├── search.py
	├── state.py
	└── treelib
	    ├── EGG-INFO
	    │   ├── PKG-INFO
	    │   ├── SOURCES.txt
	    │   ├── dependency_links.txt
	    │   ├── top_level.txt
	    │   └── zip-safe
	    └── treelib
	        ├── __init__.py
	        ├── __init__.pyc
	        ├── node.py
	        ├── node.pyc
	        ├── tree.py
	        └── tree.pyc


All pyc files are python byte code files.
The three main files for the program are the state.py, search.py, main.py

<b>main.py</b>

main.py will be the entry point of the program and handle input errors such as an invalid input.

<b>search.py</b>

search.py handles the searching for the path to the goal.
Search is defined here which is a class that takes a initial 
string representing, a search algorithm, and a cost_flag.
for a Breadth First Search a Queue is used and for all other
searches a list is used. but depending on the search the list
will be sorted.  

<b>state.py</b>

state.py defines a State class which will be represent a single
state of the board. Moves can be applied to a state. a state as a
method that can determine if it is a goal state my counting the 
number of misplaced pieces. A game is completed if it has no 
misplaced pieces. 

<b>treelib</b>

Treelib is a external library that handles creating and adding nodes to a tree. The search algorithm handles what gets into a tree.

<h3>Platform</h3>

The program was developed on Mac OSX Yosemite using Python. However it should run on any platform that can run Python programs in Python version 2.7.6

<h3>Problems</h3>

<h3>Running program</h3>
To Run the program unzip the file and in command line or similiar program the command is

python main.py <starting-board> <BFS|DFS|A-STAR|UCS|GS> [cost]

the starting board and search are required and the cost is a flag that will change the cost function to a variable cost default is constant
for example to do an a-star search on a starting board wwxbb with no variable cost, the command would be

	python main.py wwxbb A-STAR 
