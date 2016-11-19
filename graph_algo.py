import networkx as nx
from Graph import Graph

class Graph_algo:

    # loads Graph.graph instance into Graph_algo self.graph
    def __init__(self, graph):
        self.graph = graph

    # calculate the distance between two nodes
    # should return float number
    def calc_dist(self, v1, v2):
        return nx.shortest_path(self.graph, source = v1, target = v2)

    # calculate the path between two nodes
    # should return a list [v1 ..... v2] represents the path
    def calc_path(v1, v2):
        pass

    # calculates the path between two nodes
    # Without pass over the a blacklist of nodes 
    # should return a list [v1 ..... v2] represents the path 
    def calc_path_with_blacklist(self, v1, v2, *blacklist):
        pass

# main test, should be removed !
if __name__ == '__main__': 
    G = Graph('g0.txt')
    
    #print the nodes and distance between 
    for edge in G.graph.edges():
        print str(edge[0]) + " " + str(edge[1]) + " " + str(G.graph.get_edge_data(edge[0], edge[1]))
    
    print Graph_algo(G).calc_dist(0,5)