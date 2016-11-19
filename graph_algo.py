import networkx as nx

class Graph_algo:

    # loads Graph.graph instance into Graph_algo self.graph
    def __init__(self,graph):
        self.graph=graph

    # Returns the shortest path length from source to target in a weighted graph using networkx function
    # should return float number
    def calc_dist(self,v1, v2):
        return nx.dijkstra_path_length(self.graph,v1,v2)

    # calculate the path between two nodes
    # Using networkx function - should return a list [v1 ..... v2] represents the shortest path
    def calc_path(self,v1, v2):
       return nx.shortest_path(self.graph,v1,v2)

    # calculates the path between two nodes
    # Without pass over the a blacklist of nodes 
    # should return a list [v1 ..... v2] represents the path 
    def calc_path_with_blacklist(v1, v2, *blacklist):
        pass

    