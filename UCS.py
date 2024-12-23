import copy
from queue import PriorityQueue
import matplotlib.pyplot as plt
import networkx as nx
class Graph:

    #graph: Contains information of all adjacent nodes as key-value pairs
    #cost_dict: Stores the costs of all edges
    #final_cost: Contains all possible costs from the start node to the target node
    def __init__(self):
        self.graph = dict()
        self.cost_dict = dict()
        self.final_dict = dict()

    # u: Start node
    # v: Target node
    # c: Weight of the edge from u to v
    def addEdge(self, u, v, c):

        if u not in self.graph:
            qu = PriorityQueue()
            self.graph.update({u: qu})

        self.graph[u].put(v)
        self.cost_dict.update({(u, v): c})

    # To keep a list of visited nodes
    def tnode(self, n):
        self.visited = [False] * n

    def UCS_util(self, s, visited, path, goal, value):
        # To add a node to the current path
        path.append(s)
        # To mark that the node has been visited
        visited[s] = True

        # To save the path if the target node is reached
        if goal == s:
            self.final_dict.update({tuple(path): value})
            return

        # To check if the node has been visited and create a new path if not
        for i in self.graph[s].queue:
            if visited[i] == False:
                self.UCS_util(i, copy.deepcopy(visited), copy.deepcopy(path), goal, value + self.cost_dict[s, i])

    def UCS(self, s, goal):
        self.visited[s] = True
        # To keep a list of all nodes visited on the path from the start to the target
        path = [s]

        for i in self.graph[s].queue:
            if self.visited[i] == False:
                # To store transition costs
                value = self.cost_dict[s, i]
                self.UCS_util(i, copy.deepcopy(self.visited), copy.deepcopy(path), goal, value)

    # To print all paths found from the start to the target
    def all_paths(self):
        # For checking the paths
        if bool(self.final_dict):
            print("All possible routes: ")
            a = 1
            for i in self.final_dict:
                print("Route", a, ":",  i, "cost: ", self.final_dict[i])
                a +=1
        else:
            print("No path between the start and target nodes.")

    # To draw the directed and weighted graph to be worked on
    def draw_graph(self):
        G = nx.DiGraph()
        for u in self.graph:
            for v in self.graph[u].queue:
                G.add_edge(u, v, weight=self.cost_dict[u, v])
        pos = {0: (-1, 0), 1: (0, 1), 2: (-1, -2), 3: (1, 1), 4: (3, 0), 5: (1, -1), 6: (4, 1), 7: (4, -2), 8: (2, -2), 9: (2, -3)}
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, with_labels=True, node_color='steelblue', node_size=500, edge_color='steelblue',
                pos=pos, width=2, arrowsize=20)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, font_size=10)

        plt.show()

    def draw_optimal_path(self):
        if bool(self.final_dict):
            # To find the shortest route
            path = min(self.final_dict, key=self.final_dict.get)
            cost = self.final_dict[path]
            print(f"\nThe shortest route: {path}, Cost: {cost}")

            # To draw the directed graph showing the best path
            optimal_graph = nx.DiGraph()
            optimal_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            optimal_graph.add_edges_from(optimal_edges)

            # To specify the position of each node
            pos = {0: (-1, 0), 1: (0, 1), 2: (-1, -2), 3: (1, 1), 4: (3, 0), 5: (1, -1), 6: (4, 1), 7: (4, -2), 8: (2, -2), 9: (2, -3)}

            # The best route will be shown in red, unused nodes will not be displayed
            nx.draw_networkx(optimal_graph, pos=pos, with_labels=True, node_color='steelblue', node_size=300,
                             edge_color='steelblue', width=2, arrowsize=20)
            nx.draw_networkx_edges(optimal_graph, pos=pos, edgelist=optimal_edges, edge_color='red',width=2,
                                   arrowsize=20)
            plt.show()
        else:
            print("No path between the start and target nodes.")


g = Graph()
g.tnode(10)

g.addEdge(0, 1, 1)
g.addEdge(0, 2, 1)
g.addEdge(1, 3, 3)
g.addEdge(2, 5, 2)
g.addEdge(3, 6, 4)
g.addEdge(3, 5, 2)
g.addEdge(4, 6, 1)
g.addEdge(4, 7, 5)
g.addEdge(5, 4, 4)
g.addEdge(6, 7, 1)
g.addEdge(5, 0, 3)
g.addEdge(5, 8, 1)
g.addEdge(8, 4, 1)
g.addEdge(8, 9, 3)
g.addEdge(9, 7, 1)

g.UCS(0, 7)
g.draw_graph()
g.all_paths()
g.draw_optimal_path()
