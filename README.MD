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


    <h4>main.py</h4>
        <p>
            main.py will be the entry point of the program and handle input errors such as an invalid input.
        </p>
    <h4>search.py</h4>
    	<p>
    		search.py handles the searching for the path to the goal.
    		Search is defined here which is a class that takes a initial string representing, a search algorithm, and a cost_flag.
    		for a Breadth First Search a Queue is used and for all other searches a list is used. but depending on the search the list will be sorted.  
    	</p>
    <h4>state.py</h4>
    	<p>
    	state.py defines a State class which will be represent a single state of the board. Moves can be applied to a state. a state as a method that can determine if it is a goal state my counting the number of misplaced pieces. A game is completed if it has no misplaced pieces. 
    	</p>		
    <h4>treelib</h4>
    	<p>
    		Treelib is a external library that handles creating and adding nodes to a tree. The search algorithm handles what gets into a tree.
    	</p>

<h3>Platform</h3>

<h3>Problems</h3>

<h3>Running program</h3>
