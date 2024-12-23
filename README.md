# UCS (Uniform Cost Search)
 Solving and visualizing an example graph problem using the UCS (Uniform Cost Search) method. Libraries used in Python: queue, networkx, matplotlib

 In this code, a class named Graph has been created. This class has the following methods:

__init__: Initializes the graph dictionary, cost_dict dictionary, and final_dict dictionary

addEdge: Adds a new edge to the graph dictionary along with its corresponding cost in the cost_dict dictionary

tnode: Creates a list to track visited nodes

UCS_util: Recursively explores all possible paths from the start node to the target node, tracking the path and its corresponding cost

UCS: Initializes the visited list and the path list and starts the UCS_util method

all_paths: Prints all possible paths from the start node to the target node along with their corresponding costs

draw_graph: Draws the graph using the "networkx" and "matplotlib" libraries

draw_optimal_path: Finds the optimal path from final_dict and highlights it on the graph using the "networkx" and "matplotlib" libraries
