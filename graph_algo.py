import networkx as nx

class Graph_algo:

    # loads Graph.graph instance into Graph_algo self.graph
    def __init__(self,graph):
        self.graph=graph

    # calculate the distance between two nodes
    # should return float number
    def calc_dist(v1, v2):
        return self.graph.shortest_path_length(self.graph,v1,v2)

    # calculate the path between two nodes
    # should return a list [v1 ..... v2] represents the path
    def calc_path(self,v1, v2):
       return self.graph.shortest_path(self.graph,v1,v2)

    # calculates the path between two nodes
    # Without pass over the a blacklist of nodes 
    # should return a list [v1 ..... v2] represents the path 
    def calc_path_with_blacklist(v1, v2, *blacklist):
        pass

    