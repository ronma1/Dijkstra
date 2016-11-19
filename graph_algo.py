import networkx as nx
from Graph import Graph

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
       return nx.dijkstra_path(self.graph,v1,v2)

    # calculates the path between two nodes
    # Without pass over the a blacklist of nodes 
    # should return a list [v1 ..... v2] represents the path 
    def calc_path_with_blacklist(self,v1, v2, blacklist):
        for node in blacklist:
            self.graph.remove_node(node)
        return nx.dijkstra_path_length(self.graph,v1,v2)
        

    #Return the diameter of the graph G
    def diamiter(self):
        return nx.diameter(self.graph)
        
    #Return the radius of the graph G
    def radius(self):
        return nx.radius(self.graph)

    def is_Triangle_inequality(self):
        for i in range(0,nx.number_of_nodes(self.graph),1):
            for j in range(0,nx.number_of_nodes(self.graph)):
                print nx.dijkstra_path(self.graph,i,j)
                print nx.dijkstra_path_length(self.graph,i,j)
                if nx.dijkstra_path_length(self.graph,i,j)>1:
                    return False
        return True

    def time(self):
        pass

    if __name__ == '__main__': 
         g = Graph('g0.txt')
         #print calc_dist(g,0,1)
         # print calc_path(g,0,1)
         #print calc_path_with_blacklist(g,0,1,[4,3])
         print is_Triangle_inequality(g) 
